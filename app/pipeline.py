from datetime import timedelta
from time import perf_counter
from .config import START_DATE, END_DATE
from .data import load_profiles, read_cache
from .models import Request, InvalidInput
from .normalize import normalize
from .filters import rejection_reasons, REASONS, LABELS
from .scoring import SemanticIndex, score
from .facts import facts_for
from .explain.generator import Generator


class Engine:
    def __init__(self, include_team=True, profiles=None, provider=None, persistent=True):
        self.profiles = load_profiles(include_team) if profiles is None else sorted(profiles, key=lambda p: p.id)
        self.index = SemanticIndex(self.profiles, read_cache("embeddings_cache.json"))
        self.facts_cache = read_cache("facts_cache.json")
        self.generator = Generator(provider, persistent=persistent)
        self.meta = {
            "cities": sorted(dict.fromkeys(p.city for p in self.profiles)),
            "categories": sorted(dict.fromkeys(c for p in self.profiles for c in p.categories)),
            "events": sorted(dict.fromkeys(c for p in self.profiles for c in p.event_formats)),
            "languages": sorted(dict.fromkeys(c for p in self.profiles for c in p.languages)),
            "date_min": START_DATE, "date_max": END_DATE, "profile_count": len(self.profiles),
            "synthetic_count": sum(p.synthetic for p in self.profiles)
        }

    def validate(self, query):
        q = query if isinstance(query, Request) else Request.model_validate(query)
        updates = {}
        for field, key in [("city", "cities"), ("category", "categories"), ("event", "events"), ("lang", "languages")]:
            value = getattr(q, field)
            if field == "lang" and (value is None or not value.strip()):
                updates[field] = None
                continue
            allowed = self.meta[key]
            canonical = next((v for v in allowed if normalize(v) == normalize(value)), None)
            if canonical is None:
                raise InvalidInput(f"Неизвестное значение {field}: {value}. Допустимые: {', '.join(allowed)}")
            updates[field] = canonical
        if not START_DATE <= str(q.date) <= END_DATE:
            raise InvalidInput(f"Дата должна быть от {START_DATE} до {END_DATE}")
        return q.model_copy(update=updates)

    def recommend(self, query, with_hints=True):
        started = perf_counter()
        q = self.validate(query)
        scoped = [p for p in self.profiles if p.city == q.city and q.category in p.categories]
        trace = [{"step": "load_normalize", "profiles": len(self.profiles)}, {"step": "scope", "count": len(scoped)}]
        counts = {r: 0 for r in REASONS}
        passed, excluded = [], []
        for p in scoped:
            reasons = rejection_reasons(p, q)
            if reasons:
                counts[reasons[0]["reason"]] += 1
                excluded.append({"id": p.id, "primary_reason": reasons[0]["reason"], "all_reasons": reasons})
            else:
                passed.append(p)
        trace.append({"step": "hard_filters", "passed": len(passed), "excluded": excluded, "counts": counts})
        filter_done = perf_counter()
        ranked = [(p, score(p, q, self.index)) for p in passed]
        ranked.sort(key=lambda row: (-row[1]["score"], row[0].price_from_kzt, row[0].id))
        selected = ranked[:3]
        trace.append({"step": "scoring", "candidates": [{"id": p.id, **s} for p, s in ranked]})
        scoring_done = perf_counter()
        facts = [facts_for(p, q, [x[0] for x in selected], self.facts_cache) for p, s in selected]
        texts, explanation_trace = self.generator.generate(q, facts) if facts else ([], {"backend": "none"})
        trace.append({"step": "explanation", "facts": facts, **explanation_trace})
        cards = []
        from .normalize import money
        for (p, s), text in zip(selected, texts):
            quality = []
            if p.price_imputed:
                quality.append("Цена проставлена при подготовке данных, уточните у подрядчика")
            if p.city_imputed:
                quality.append("Город проставлен при подготовке данных, уточните у подрядчика")
            cards.append({"id": p.id, "anon_name": p.anon_name, "category": q.category,
                "city": p.city, "price": money(p.price_from_kzt), "price_from_kzt": p.price_from_kzt,
                "explanation": text, "score": s["score"],
                "badge": "синтетический (наш)" if p.source == "team" else ("синтетический (датасет)" if p.synthetic else "реальный"),
                "synthetic": p.synthetic, "data_quality_note": "; ".join(quality)})
        n = len(cards)
        status = "MATCHED" if n else ("NONE_PASS_CONDITIONS" if scoped else "NO_CATEGORY_IN_CITY")
        title = f"Подобрали {n}" if n else ("Никто не проходит по условиям" if scoped else "В городе нет этой категории")
        date_text = q.date.strftime("%d.%m.%Y")
        breakdown = "; ".join(f"{LABELS[r]} — {counts[r]}" for r in REASONS if counts[r])
        summary = f'В городе {q.city}, категория «{q.category}»: всего {len(scoped)}, проходят {len(passed)}. '
        if n:
            summary += f"Подобрали {n}. "
            if n < 3:
                summary += f"Найдено {n} — меньше трёх: " + (breakdown or f"в каталоге города всего {len(scoped)} профиля этой категории") + ". "
        elif scoped:
            summary += "Ни один кандидат не проходит: " + breakdown + ". "
        else:
            summary += "В этом городе нет ни одного профиля запрошенной категории. "
        summary += f"Исключено из-за занятости на {date_text}: {counts['busy']}."
        if q.date.month == 12 and counts["busy"] >= len(scoped)/2 and counts["busy"]:
            summary += f" Высокая загрузка на эту декабрьскую дату: заняты {counts['busy']} из {len(scoped)}."
        explanation_done = perf_counter()
        hints = self.hints(q, scoped, excluded) if with_hints and n < 3 else []
        finished = perf_counter()
        return {"status": status, "title": title, "summary": summary, "cards": cards, "hints": hints,
            "counts": {"scope": len(scoped), "passed": len(passed), "excluded": len(excluded), "reasons": counts},
            "trace": trace, "timings_ms": {"filters": round((filter_done-started)*1000, 3),
            "scoring": round((scoring_done-filter_done)*1000, 3), "explanations": round((explanation_done-scoring_done)*1000, 3),
            "hints": round((finished-explanation_done)*1000, 3), "total": round((finished-started)*1000, 3)}}

    def hints(self, q, scoped, excluded):
        hints = []
        if not scoped:
            cities = sorted(dict.fromkeys(p.city for p in self.profiles if q.category in p.categories))
            return ["Категория есть в городах: " + ", ".join(cities)] if cities else []
        dates = []
        for offset in sorted([n for n in range(-7, 8) if n], key=lambda n: (abs(n), n)):
            day = q.date+timedelta(days=offset)
            if START_DATE <= str(day) <= END_DATE:
                count = sum(not rejection_reasons(p, q.model_copy(update={"date": day})) for p in scoped)
                if count:
                    dates.append(f"{day.strftime('%d.%m.%Y')} — подходят {count}")
        if dates:
            hints.append("При остальных условиях без изменений: " + "; ".join(dates[:3]) + ".")
        budget_only = [p for p in scoped if [r["reason"] for r in rejection_reasons(p, q)] == ["budget"] and p.price_from_kzt is not None]
        if budget_only:
            price = min(p.price_from_kzt for p in budget_only)
            from .normalize import money
            hints.append(f"Ещё один кандидат прошёл бы при бюджете от {money(price)}: сейчас не хватает {money(price-q.budget)}.")
        ordered = sorted(excluded, key=lambda e: (-score(next(p for p in scoped if p.id == e["id"]), q, self.index)["score"], e["id"]))
        for item in ordered[:2]:
            if item["primary_reason"] == "busy":
                p = next(p for p in scoped if p.id == item["id"])
                future = next((q.date+timedelta(days=n) for n in range(1, 8) if str(q.date+timedelta(days=n)) <= END_DATE and not rejection_reasons(p, q.model_copy(update={"date": q.date+timedelta(days=n)}))), None)
                if future:
                    hints.append(f"Один из исключённых кандидатов занят {q.date.strftime('%d.%m.%Y')}, но прошёл бы все условия {future.strftime('%d.%m.%Y')}.")
        return hints

    def compare(self, query, second_date):
        q = self.validate(query)
        other = self.validate(q.model_copy(update={"date": second_date}))
        first, second = self.recommend(q), self.recommend(other)
        left_ids = [c["id"] for c in first["cards"]]
        right_ids = [c["id"] for c in second["cards"]]
        diff = []
        for side, cards, target, remaining in [("выпал", first["cards"], other, right_ids), ("появился", second["cards"], q, left_ids)]:
            for card in cards:
                if card["id"] not in remaining:
                    p = next(p for p in self.profiles if p.id == card["id"])
                    reason = f"занят {target.date.strftime('%d.%m.%Y')}" if target.date in p.busy_dates else "изменился состав top-3 из-за доступности других кандидатов"
                    diff.append({"id": p.id, "anon_name": p.anon_name, "change": side, "reason": reason})
        return {"first": first, "second": second, "diff": diff}
