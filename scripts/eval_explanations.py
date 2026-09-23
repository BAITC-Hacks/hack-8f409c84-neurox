import argparse
import itertools
import json
import math
import os
import statistics
from collections import Counter
from dotenv import load_dotenv
from app.pipeline import Engine
from app.config import ROOT
from app.explain.critic import check
from app.llm import OpenAIProvider


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--live",action="store_true",help="Explicitly send facts to OpenAI and incur API usage")
    args=p.parse_args()
    load_dotenv(ROOT/".env")
    provider=None
    if args.live:
        if not os.getenv("OPENAI_API_KEY"):p.error("--live requires OPENAI_API_KEY")
        provider=OpenAIProvider(os.environ["OPENAI_API_KEY"],os.getenv("OPENAI_MODEL","gpt-4o-mini"))
    e=Engine(provider=provider, persistent=False)
    if args.live:
        queries=json.loads((ROOT/"data/demo_queries.json").read_text(encoding="utf-8"))
    else:
        queries=[dict(city=city,category=cat,event=ev,date=day,budget=2000000)
                 for city,cat,ev,day in itertools.product(e.meta["cities"],e.meta["categories"],e.meta["events"],["2026-10-01","2026-11-14","2026-12-26"])]
    total=grounded=stop=request=blind=0
    timings=[]
    backends=Counter()
    for q in queries:
        e.generator.cache.clear() # Measure generation, not previously committed demo cache.
        r=e.recommend(q)
        timings.append(r["timings_ms"]["total"])
        facts=r["trace"][-1]["facts"]
        backends[r["trace"][-1]["backend"]]+=1
        for c,f in zip(r["cards"],facts):
            errors=check(c["explanation"],f)
            total+=1
            grounded+=not errors
            stop+="stop_phrase" in errors
            request+=f["event"] in c["explanation"]
            anonymous=c["explanation"]
            for profile in e.profiles:anonymous=anonymous.replace(profile.anon_name,"[имя удалено]")
            blind+=sum(bool(other["detail"]) and other["detail"] in anonymous for other in facts)==1
    timings.sort()
    metrics={"mode":"live" if args.live else "offline", "queries":len(queries),"explanations":total,
             "critic_pass_rate":grounded/max(total,1),"stop_phrase_rate":stop/max(total,1),
             "request_parameter_rate":request/max(total,1),"blind_attribution_rate":blind/max(total,1),
             "fallback_query_rate":backends["fallback"]/max(1,sum(v for k,v in backends.items() if k!="none")),
             "backends":dict(backends),"latency_p50_ms":round(statistics.median(timings),3),
             "latency_p95_ms":timings[math.ceil(len(timings)*.95)-1]}
    path=ROOT/("docs/EVAL_LIVE.md" if args.live else "docs/EVAL.md")
    text="# Проверка объяснений\n\n"+("Реальные вызовы OpenAI, без кэша.\n" if args.live else "Офлайн-измерение без API-ключа и без сетевых вызовов. Живой API не проверялся.\n")
    text+="\n```json\n"+json.dumps(metrics,ensure_ascii=False,indent=2)+"\n```\n\nМетодика: сетка запросов (либо 10 демо-запросов для --live), кэш текста очищается перед каждым запросом. Grounding измеряется критиком с закрытой грамматикой; blind attribution сопоставляет дословные уникальные фрагменты описаний без имён. Это автоматическая проверка, не независимая человеческая оценка. Latency не включает старт процесса и загрузку данных.\n"
    path.write_text(text,encoding="utf-8")
    print(json.dumps(metrics,ensure_ascii=False,indent=2))


if __name__=="__main__":main()
