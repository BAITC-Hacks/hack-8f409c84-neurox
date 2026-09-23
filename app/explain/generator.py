import hashlib
import json
import sqlite3
from pathlib import Path
from queue import Queue, Empty
from threading import Lock, Thread
from ..data import read_cache
from ..llm import OfflineProvider
from .templates import options
from .critic import check, pairwise_similarity
from ..config import CONFIG, ROOT

VERSION = "grounded-plan-v2"


class Generator:
    def __init__(self, provider=None, persistent=True):
        self.provider = provider or OfflineProvider()
        self.cache = read_cache("explanations_cache.json")
        self.lock = Lock()
        self.persistent = persistent
        self.db_path = ROOT / ".cache/explanations.sqlite3"
        if persistent:
            self.db_path.parent.mkdir(exist_ok=True)
            with sqlite3.connect(self.db_path) as db:
                db.execute("CREATE TABLE IF NOT EXISTS explanations (key TEXT PRIMARY KEY, text TEXT NOT NULL)")

    def cached(self, key):
        with self.lock:
            saved = self.cache.get(key)
        if saved or not self.persistent:
            return saved
        with sqlite3.connect(self.db_path) as db:
            row = db.execute("SELECT text FROM explanations WHERE key = ?", (key,)).fetchone()
        return json.loads(row[0]) if row else None

    def remember(self, key, texts):
        if self.persistent:
            with sqlite3.connect(self.db_path) as db:
                db.execute("INSERT OR IGNORE INTO explanations VALUES (?, ?)", (key, json.dumps(texts, ensure_ascii=False)))
                texts = json.loads(db.execute("SELECT text FROM explanations WHERE key = ?", (key,)).fetchone()[0])
        with self.lock:
            if len(self.cache) > 2048:
                self.cache.clear()
            self.cache[key] = texts
        return texts

    def choose(self, rows, errors):
        if isinstance(self.provider, OfflineProvider):
            return self.provider.choose(rows, errors)
        result = Queue()
        def call():
            try:
                result.put((True, self.provider.choose(rows, errors)))
            except Exception as exc:
                result.put((False, exc))
        Thread(target=call, daemon=True).start()
        try:
            ok, value = result.get(timeout=3.0)
        except Empty:
            raise TimeoutError("Explanation deadline exceeded") from None
        if not ok:
            raise value
        return value

    def generate(self, query, facts):
        key = hashlib.sha256(json.dumps([VERSION, query.model_dump(mode="json"), facts], ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        texts = self.cached(key)
        if texts and len(texts) == len(facts) and all(not check(t, f) for t, f in zip(texts, facts)):
            return texts, {"backend": "cache", "cache_key": key, "critic_errors": []}
        rows = [{"facts": f, "options": options(f)} for f in facts]
        errors = []
        backend = "offline" if isinstance(self.provider, OfflineProvider) else "openai-plan"
        texts = []
        for attempt in range(2):
            try:
                choices = self.choose(rows, errors)
                if len(choices) != len(facts) or any(type(n) is not int or n not in (0, 1) for n in choices):
                    raise ValueError("invalid_plan")
                texts = [options(f)[n] for f, n in zip(facts, choices)]
                errors = [error for t, f in zip(texts, facts) for error in check(t, f)]
                if not errors:
                    break
            except Exception as exc:
                errors = [type(exc).__name__]
                if not isinstance(exc, ValueError):
                    break
        if errors or not texts:
            texts = [options(f)[i % 2] for i, f in enumerate(facts)]
            backend = "fallback"
        final_errors = [error for t, f in zip(texts, facts) for error in check(t, f)]
        similarities = [round(pairwise_similarity(texts[i], texts[j]), 4) for i in range(len(texts)) for j in range(i+1, len(texts))]
        if any(s >= CONFIG["similarity_threshold"] for s in similarities):
            final_errors.append("similarity_threshold")
        texts = self.remember(key, texts)
        return texts, {"backend": backend, "cache_key": key, "provider_errors": errors,
                       "critic_errors": final_errors, "pairwise_similarity": similarities}
