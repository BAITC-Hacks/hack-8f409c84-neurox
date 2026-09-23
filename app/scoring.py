"""No API calls, random state, hash-order iteration, or mutable ranking inputs."""
from collections import Counter
import hashlib
import json
import math
import re
from .config import CONFIG
from .normalize import normalize


def tokens(text):
    return re.findall(r"[a-zа-я0-9]+", normalize(text))


def fingerprint(profiles):
    payload = [p.model_dump(mode="json") for p in profiles]
    return hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def query_key(q):
    return " | ".join([q.event, q.category] + ([q.lang] if q.lang else []))


def cosine(a, b):
    if len(a) != len(b) or not a:
        return 0.0
    denominator = math.sqrt(sum(x*x for x in a) * sum(x*x for x in b))
    return sum(x*y for x, y in zip(a, b)) / denominator if denominator else 0.0


class SemanticIndex:
    def __init__(self, profiles, cache):
        self.profiles = profiles
        self.cache = cache if cache.get("dataset_sha256") == fingerprint(profiles) else {}
        documents = [tokens(p.description) for p in profiles]
        self.vocab = sorted(dict.fromkeys(t for document in documents for t in document))
        self.idf = [math.log((1+len(documents))/(1+sum(t in d for d in documents)))+1 for t in self.vocab]
        self.vectors = {p.id: self.vector(p.description) for p in profiles}

    def vector(self, text):
        counts = Counter(tokens(text))
        return [counts[t]*weight for t, weight in zip(self.vocab, self.idf)]

    def similarity(self, p, q):
        stored = self.cache.get("profiles", {}).get(p.id)
        query = self.cache.get("queries", {}).get(query_key(q))
        if stored and query:
            return cosine(stored, query), self.cache.get("model", "cached")
        return cosine(self.vectors[p.id], self.vector(query_key(q))), "tfidf-fallback"


def score(p, q, index):
    ratio = (p.price_from_kzt or 0) / q.budget
    semantic, backend = index.similarity(p, q)
    parts = {"budget_fit": max(0.0, 1.0-abs(ratio-0.75)/0.75), "semantic_fit": semantic}
    if q.lang is not None:
        parts["language_fit"] = float(q.lang in p.languages)
    if q.hours is not None:
        parts["hours_fit"] = 1.0 if p.max_hours is None else min(1.0, p.max_hours/q.hours)
    weights = CONFIG["weights"]
    quality = CONFIG["quality_penalty"] * (int(p.price_imputed)+int(p.city_imputed))
    value = sum(parts[k]*weights[k] for k in sorted(parts))/sum(weights[k] for k in sorted(parts))-quality
    return {"score": round(value, 4), "components": parts, "data_quality_penalty": quality, "semantic_backend": backend}
