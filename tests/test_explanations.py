import itertools
from unittest.mock import Mock
from app.pipeline import Engine
from app.explain.critic import check, normalize_numbers, pairwise_similarity
from app.config import CONFIG


def test_grid_grounding_and_blind_matching(engine):
    checked = 0
    for city, category, event, day in itertools.product(engine.meta["cities"],engine.meta["categories"],engine.meta["events"],["2026-10-01","2026-11-14","2026-12-26"]):
        q = dict(city=city,category=category,event=event,date=day,budget=2000000)
        result = engine.recommend(q,with_hints=False)
        facts = result["trace"][-1]["facts"]
        for card, own in zip(result["cards"],facts):
            assert not check(card["explanation"],own), (card,check(card["explanation"],own))
            # Neither identity nor card order participates in the blind attribution.
            anonymous = card["explanation"]
            for profile in engine.profiles:
                anonymous = anonymous.replace(profile.anon_name, "[имя удалено]")
            matching = [f["id"] for f in reversed(facts) if (f["detail"] and f["detail"] in anonymous)]
            assert matching == [card["id"]], (card,matching)
            checked += 1
        for a,b in itertools.combinations(result["cards"],2):
            assert pairwise_similarity(a["explanation"],b["explanation"]) < CONFIG["similarity_threshold"]
    assert checked > 100


def test_mock_llm_invalid_then_valid(query):
    provider = Mock()
    provider.choose.side_effect = [ValueError("bad response"), [1,0,1]]
    engine = Engine(provider=provider, persistent=False)
    engine.generator.cache.clear()
    r = engine.recommend(query)
    assert provider.choose.call_count == 2
    assert r["trace"][-1]["backend"] == "openai-plan"
    assert not r["trace"][-1]["critic_errors"]


def test_timeout_fallback_and_reject_hallucinations(query):
    provider = Mock()
    provider.choose.side_effect = TimeoutError()
    engine = Engine(provider=provider, persistent=False)
    engine.generator.cache.clear()
    r = engine.recommend(query)
    assert provider.choose.call_count == 1
    assert r["trace"][-1]["backend"] == "fallback"
    for c,f in zip(r["cards"],r["trace"][-1]["facts"]):
        assert not check(c["explanation"],f)
        assert check(c["explanation"]+" Гарантирует 999999 гостей.",f)
        assert check(c["explanation"].replace("Цена","Отличный выбор"),f) or "Цена" not in c["explanation"]


def test_numeric_normalization():
    for s in ("70 000", "70000", "70 тыс.", "70 тыс. ₸"):
        assert "70000" in normalize_numbers(s)
