from datetime import date, timedelta
from app.filters import rejection_reasons
from app.models import Request


def test_primary_reason_precedence(engine):
    p = engine.profiles[0].model_copy(update={"price_from_kzt":None,"max_hours":1,"languages":[],"event_formats":[]})
    q = Request(city=p.city, category=p.categories[0], event="корпоратив", date=p.busy_dates[0],budget=1,hours=8,lang="казахский")
    assert [r["reason"] for r in rejection_reasons(p,q)] == ["busy","format","budget","language","hours"]
    assert rejection_reasons(p,q)[2]["missing_price"]


def test_no_padding_hints_and_arithmetic(engine, query):
    for city in engine.meta["cities"]:
        for category in engine.meta["categories"]:
            r = engine.recommend({**query,"city":city,"category":category})
            c = r["counts"]
            assert c["passed"]+c["excluded"] == c["scope"]
            assert c["excluded"] == sum(c["reasons"].values())
            assert len(r["cards"]) == min(c["passed"],3)
            for p in engine.profiles:
                assert p.anon_name not in "\n".join(r["hints"])
            for card in r["cards"]:
                p = next(p for p in engine.profiles if p.id==card["id"])
                if p.price_imputed or p.city_imputed:
                    assert card["data_quality_note"]


def test_compare_reasons(engine,query):
    original = engine.recommend(query)
    other = date.fromisoformat(query["date"])+timedelta(days=1)
    r = engine.compare(query,other)
    allowed_ids = [c["id"] for c in r["first"]["cards"]+r["second"]["cards"]]
    for item in r["diff"]:
        assert item["id"] in allowed_ids
        assert "занят" in item["reason"] or "доступности" in item["reason"]


def test_single_change_budget_hint_is_sufficient(engine,query):
    low = engine.validate({**query,"budget":1})
    r = engine.recommend(low)
    eligible = [p for p in engine.profiles if p.city==low.city and low.category in p.categories and [x["reason"] for x in rejection_reasons(p,low)]==["budget"]]
    if eligible:
        min_price = min(p.price_from_kzt for p in eligible)
        assert engine.recommend(low.model_copy(update={"budget":min_price}))["cards"]
        assert any("при бюджете" in h for h in r["hints"])
