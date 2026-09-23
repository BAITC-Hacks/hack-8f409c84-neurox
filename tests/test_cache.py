from unittest.mock import Mock
from app.pipeline import Engine
from app.explain.generator import Generator


def test_persistent_text_cache(query, tmp_path):
    provider=Mock()
    provider.choose.return_value=[1,0,1]
    e=Engine(provider=provider)
    e.generator.db_path=tmp_path/"cache.sqlite3"
    import sqlite3
    with sqlite3.connect(e.generator.db_path) as db:
        db.execute("CREATE TABLE explanations (key TEXT PRIMARY KEY, text TEXT NOT NULL)")
    e.generator.cache.clear()
    first=e.recommend(query)
    assert provider.choose.call_count==1
    e2=Engine(provider=Mock())
    e2.generator.db_path=e.generator.db_path
    e2.generator.cache.clear()
    second=e2.recommend(query)
    assert second["cards"]==first["cards"]
    assert second["trace"][-1]["backend"]=="cache"
    e2.generator.provider.choose.assert_not_called()
