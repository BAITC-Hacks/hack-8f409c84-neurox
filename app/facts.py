import hashlib
import re
from .config import CONFIG
from .normalize import normalize


def description_hash(p):
    return hashlib.sha256(p.description.encode()).hexdigest()


def detail_candidates(p):
    # Exact source spans, not generated claims. Avoid boilerplate and sentence punctuation.
    parts = re.split(r"[.!?\n•;]+", p.description)
    clean = [re.sub(r"\s+", " ", s).strip(' ,:–—-') for s in parts]
    result = []
    for phrase in clean:
        if len(phrase) < 24 or re.search(r"(?<!\w)" + re.escape(normalize(p.anon_name)) + r"(?!\w)", normalize(phrase)) or "меня зовут" in normalize(phrase) or any(normalize(s) in normalize(phrase) for s in CONFIG["stop_phrases"]):
            continue
        words = phrase.split()
        phrase = " ".join(words[:24])
        if len(words) > 24:
            phrase += "…"
        if phrase not in result:
            result.append(phrase)
    return sorted(result, key=lambda text: (-len(text.split()), text))[:12]


def facts_for(p, q, peers, cache):
    saved = cache.get(p.id, {})
    candidates = saved.get("details", []) if saved.get("description_sha256") == description_hash(p) else detail_candidates(p)
    candidates = [d for d in candidates if d.rstrip("…") in re.sub(r"\s+", " ", p.description)]
    unique = [d for d in candidates if all(d.rstrip("…") not in re.sub(r"\s+", " ", other.description) for other in peers if other.id != p.id)]
    detail = (unique or candidates or [""])[0]
    others = [x.price_from_kzt for x in peers if x.id != p.id]
    return {"id": p.id, "price": p.price_from_kzt, "budget": q.budget,
            "saving": q.budget-p.price_from_kzt, "event": q.event,
            "lang": q.lang, "hours": q.hours, "max_hours": p.max_hours,
            "detail": detail, "details": candidates[:3], "unique_detail": bool(unique),
            "price_unique": p.price_from_kzt not in others,
            "more_than_cheapest": p.price_from_kzt-min([p.price_from_kzt]+others),
            "cheaper_than_others": bool(others) and p.price_from_kzt < min(others),
            "indistinguishable": not unique and p.price_from_kzt in others}
