"""Discover reproducible demo cases from the actual repository data."""
import hashlib
import json
import os
import subprocess
import sys
from datetime import date, timedelta
from app.pipeline import Engine
from app.config import ROOT


def digest(result):
    return hashlib.sha256("|".join(c["id"] for c in result["cards"]).encode()).hexdigest()


def scenarios(engine):
    base = dict(city="Алматы", date="2026-10-01", event="свадьба", category="Фотограф",budget=2000000)
    dense = None
    for city in engine.meta["cities"]:
        for cat in ("Фотограф","Ведущий","Банкетный зал"):
            for offset in range(69):
                q = {**base,"city":city,"category":cat,"date":str(date(2026,9,23)+timedelta(days=offset))}
                r = engine.recommend(q,with_hints=False)
                if r["counts"]["passed"]>3:
                    dense=q
                    break
            if dense:break
        if dense:break
    if dense is None:raise RuntimeError("Dataset has no dense scenario")
    rare = None
    for p in engine.profiles:
        for cat in p.categories:
            if sum(cat in x.categories for x in engine.profiles)==3:
                for offset in range(69):
                    q = dict(city=p.city,category=cat,event=p.event_formats[0],date=str(date(2026,9,23)+timedelta(days=offset)),budget=2000000)
                    if engine.recommend(q,with_hints=False)["cards"]:
                        rare=q
                        break
            if rare:break
        if rare:break
    absent = next({**base,"city":city,"category":cat} for city in engine.meta["cities"] for cat in engine.meta["categories"] if not any(p.city==city and cat in p.categories for p in engine.profiles))
    first = engine.recommend(dense)
    other = next(str(date(2026,9,23)+timedelta(days=i)) for i in range(100) if digest(engine.recommend({**dense,"date":str(date(2026,9,23)+timedelta(days=i))},with_hints=False))!=digest(first))
    return [("Плотная категория",dense),("Редкая категория",rare),("Никто не проходит",{**dense,"budget":1}),("Нет категории в городе",absent)], other


def write_result(lines,label,q,result):
    lines += [f"## {label}", "", "```json", json.dumps(q,ensure_ascii=False), "```", "", f"**{result['status']}** · {result['timings_ms']['total']:.2f} мс", "", result["summary"], ""]
    for c in result["cards"]:
        lines += [f"### {c['anon_name']} · {c['category']} · {c['city']} · от {c['price']}", "",f"{c['badge']} · score {c['score']}", "",c["explanation"], ""]
        if c["data_quality_note"]:lines += [c["data_quality_note"],""]
    for h in result["hints"]:lines += ["Подсказка: "+h,""]
    lines += ["<details><summary>Trace и timings</summary>","", "```json", json.dumps({"trace":result["trace"],"timings_ms":result["timings_ms"]},ensure_ascii=False,indent=2), "```", "</details>", ""]


def main():
    engine=Engine(persistent=False)
    engine.generator.cache.clear()
    cases, second_date=scenarios(engine)
    lines=["# Живое демо", "", "Источник: 66 профилей организаторов; собственная синтетика не добавлена.", ""]
    for label,q in cases:
        r=engine.recommend(q)
        write_result(lines,label,q,r)
        print(label+": "+r["status"]+f"; cards={len(r['cards'])}; {r['timings_ms']['total']:.2f} ms")
    comparison=engine.compare(cases[0][1],date.fromisoformat(second_date))
    lines += ["## Две даты","",comparison["first"]["summary"],"",comparison["second"]["summary"],"", "```json",json.dumps(comparison["diff"],ensure_ascii=False,indent=2),"```",""]
    hashes=[digest(engine.recommend(cases[0][1])) for _ in range(3)]
    args=[sys.executable,"-m","app.cli","--json"]
    for key,value in cases[0][1].items():args.extend(["--"+key,str(value)])
    env=dict(os.environ,PYTHONIOENCODING="utf-8",OPENAI_API_KEY="",LLM_PROVIDER="offline",PYTHONHASHSEED="77")
    fresh=json.loads(subprocess.check_output(args,cwd=ROOT,env=env,encoding="utf-8"))
    hashes.append(digest(fresh))
    assert all(x==hashes[0] for x in hashes)
    lines += ["## Детерминизм","", "Три вызова и новый процесс без API-ключа: четыре одинаковых SHA-256 списка id.", "", "```",*hashes,"```"]
    (ROOT/"docs/demo_output.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    sample_queries=[q for _,q in cases]
    for p in engine.profiles:
        free=next(date(2026,9,23)+timedelta(days=i) for i in range(100) if date(2026,9,23)+timedelta(days=i) not in p.busy_dates)
        sample_queries.append(dict(city=p.city,category=p.categories[0],event=p.event_formats[0],date=str(free),budget=max(p.price_from_kzt or 1,1000000),hours=3,lang=p.languages[0] if p.languages else None))
        if len(sample_queries)==10:break
    samples=["# Объяснения: 10 запросов", "", "Полные выдачи с trace; текст автоматически получен из текущего кода и данных.", ""]
    for i,q in enumerate(sample_queries,1):write_result(samples,f"Запрос {i}",q,engine.recommend(q))
    (ROOT/"docs/EXPLANATION_SAMPLES.md").write_text("\n".join(samples)+"\n",encoding="utf-8")
    (ROOT/"data/demo_queries.json").write_text(json.dumps(sample_queries,ensure_ascii=False,indent=2),encoding="utf-8")
    (ROOT/"data/explanations_cache.json").write_text(json.dumps(engine.generator.cache,ensure_ascii=False,indent=2,sort_keys=True),encoding="utf-8")
    print("Comparison date:",second_date,"diff:",len(comparison["diff"]))
    print("Determinism SHA256:",hashes[0],"(4/4 identical)")
    print("Saved docs/demo_output.md, docs/EXPLANATION_SAMPLES.md and demo text cache.")


if __name__=="__main__":main()
