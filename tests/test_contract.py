import itertools
import json
import os
import subprocess
import sys
from datetime import date, timedelta
import pytest
from app.pipeline import Engine
from app.models import Request
from app.filters import rejection_reasons
from app.explain.critic import sentences


def test_r1(engine, query):
    p = next(p for p in engine.profiles if p.max_hours is None)
    free = next(date(2026,9,23)+timedelta(days=i) for i in range(100) if date(2026,9,23)+timedelta(days=i) not in p.busy_dates)
    q = Request(city=p.city, date=free, event=p.event_formats[0], category=p.categories[0], budget=p.price_from_kzt, hours=999)
    assert not rejection_reasons(p, q)
    q = q.model_copy(update={"budget":p.price_from_kzt-1})
    assert rejection_reasons(p, q)[0]["reason"] == "budget"
    for city in engine.meta["cities"]:
        engine.recommend({**query,"city":city})
    original = engine.recommend(query)
    assert original["cards"] == engine.recommend({**query, "hours":None, "lang":None})["cards"]
    assert original["cards"] == engine.recommend({**query, "city":"  аЛмАты  ", "category":"фотограф"})["cards"]
    assert all("hours_fit" not in x["components"] and "language_fit" not in x["components"] for x in original["trace"][3]["candidates"])


def test_r2(engine, query):
    result = engine.recommend(query)
    assert 1 <= len(result["cards"]) <= 3
    for card in result["cards"]:
        assert card["category"] == query["category"]
        assert card["price"].endswith(" ₸")
        assert 1 <= len(sentences(card["explanation"])) <= 2
        assert card["badge"] in ("реальный","синтетический (датасет)","синтетический (наш)")


@pytest.mark.parametrize("include_team", [True,False])
def test_r3(include_team):
    engine = Engine(include_team=include_team)
    # Full date × city × category × format grid, including every venue and synthetic profile.
    for city, cat, event in itertools.product(engine.meta["cities"],engine.meta["categories"],engine.meta["events"]):
        scoped = [p for p in engine.profiles if p.city==city and cat in p.categories]
        for offset in range(100):
            day = date(2026,9,23)+timedelta(days=offset)
            q = Request(city=city, category=cat, event=event, date=day, budget=100000000)
            for p in scoped:
                reasons = rejection_reasons(p,q)
                if day in p.busy_dates:
                    assert reasons and reasons[0]["reason"] == "busy"
        for day in ("2026-09-23","2026-11-14","2026-12-26"):
            r = engine.recommend(dict(city=city,category=cat,event=event,date=day,budget=100000000),with_hints=False)
            assert all(date.fromisoformat(day) not in next(p.busy_dates for p in scoped if p.id==c["id"]) for c in r["cards"])


def test_r4(engine, query):
    r = engine.recommend({**query,"category":"Флорист"})
    c = r["counts"]
    assert c["passed"]+sum(c["reasons"].values()) == c["scope"]
    assert len(r["cards"]) == min(3,c["passed"])
    if r["cards"]:
        assert "меньше трёх" in r["summary"]
    assert f"занятости на 01.10.2026: {c['reasons']['busy']}" in r["summary"]


@pytest.mark.parametrize("include_team", [True,False])
def test_r5(engine, query, monkeypatch, include_team):
    e = Engine(include_team=include_team)
    expected = e.recommend(query)["cards"]
    for _ in range(3):
        assert e.recommend(query)["cards"] == expected
    monkeypatch.setenv("OPENAI_API_KEY","test-not-a-real-key")
    assert Engine(include_team=include_team).recommend(query)["cards"] == expected
    args = [sys.executable,"-m","app.cli","--city",query["city"],"--date",query["date"],"--event",query["event"],"--category",query["category"],"--budget",str(query["budget"]),"--json"]
    if not include_team:
        args.append("--no-team-synthetic")
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONHASHSEED="127", OPENAI_API_KEY="")
    actual = json.loads(subprocess.check_output(args,env=env,encoding="utf-8"))
    assert actual["cards"] == expected
    sorted_cards = sorted(expected,key=lambda c:(-c["score"],c["price_from_kzt"],c["id"]))
    assert expected == sorted_cards


@pytest.mark.parametrize("include_team", [True,False])
def test_r6(query, include_team):
    e = Engine(include_team=include_team)
    assert e.recommend(query)["status"]=="MATCHED"
    assert e.recommend({**query,"budget":1})["status"]=="NONE_PASS_CONDITIONS"
    absent = next((city,cat) for city in e.meta["cities"] for cat in e.meta["categories"] if not any(p.city==city and cat in p.categories for p in e.profiles))
    r = e.recommend({**query,"city":absent[0],"category":absent[1]})
    assert r["status"]=="NO_CATEGORY_IN_CITY" and r["summary"] and r["cards"]==[]
