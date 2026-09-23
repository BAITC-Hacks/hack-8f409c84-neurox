"""Explicit build step; never invoked during recommendation."""
import argparse
import itertools
import json
import os
import httpx
from dotenv import load_dotenv
from app.pipeline import Engine
from app.scoring import fingerprint
from app.config import ROOT
from app.facts import detail_candidates, description_hash


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=["tfidf", "openai"], default="tfidf")
    args = parser.parse_args()
    load_dotenv(ROOT / ".env")
    engine = Engine()
    keys = sorted(" | ".join([e,c]+([lang] if lang else [])) for e,c,lang in itertools.product(engine.meta["events"], engine.meta["categories"], [None]+engine.meta["languages"]))
    texts = [p.description for p in engine.profiles]+keys
    if args.provider == "openai":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            parser.error("OPENAI_API_KEY is required for --provider openai")
        vectors = []
        with httpx.Client(timeout=60) as client:
            for offset in range(0,len(texts),64):
                response = client.post("https://api.openai.com/v1/embeddings", headers={"Authorization": f"Bearer {api_key}"}, json={"model":"text-embedding-3-small","input":texts[offset:offset+64]})
                response.raise_for_status()
                vectors.extend(item["embedding"] for item in sorted(response.json()["data"], key=lambda x:x["index"]))
        model = "text-embedding-3-small"
    else:
        vectors = [engine.index.vector(t) for t in texts]
        model = "tfidf-local-v1"
    n = len(engine.profiles)
    cache = {"model":model, "dataset_sha256":fingerprint(engine.profiles),
             "profiles":{p.id:v for p,v in zip(engine.profiles,vectors[:n])}, "queries":dict(zip(keys,vectors[n:]))}
    (ROOT/"data/embeddings_cache.json").write_text(json.dumps(cache,ensure_ascii=False,separators=(",",":")),encoding="utf-8")
    facts = {p.id:{"description_sha256":description_hash(p),"details":detail_candidates(p),"source":"exact-description-spans"} for p in engine.profiles}
    (ROOT/"data/facts_cache.json").write_text(json.dumps(facts,ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"Built {model}: {n} profiles, {len(keys)} queries; grounded facts cached.")

if __name__ == "__main__":
    main()
