"""Lossless typed conversion of the organizer CSV."""
import argparse
import csv
import json
from pathlib import Path

def convert(source, destination):
    rows = []
    with Path(source).open(encoding="utf-8-sig", newline="") as stream:
        for row in csv.DictReader(stream):
            for key in ("categories", "event_formats", "languages", "busy_dates"):
                row[key] = row[key].split("|") if row[key] else []
            for key in ("synthetic", "city_imputed", "price_imputed"):
                row[key] = row[key].lower() == "true"
            row["price_from_kzt"] = int(row["price_from_kzt"]) if row["price_from_kzt"] else None
            row["max_hours"] = float(row["max_hours"]) if row["max_hours"] else None
            rows.append(row)
    Path(destination).parent.mkdir(parents=True, exist_ok=True)
    Path(destination).write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows)+"\n", encoding="utf-8")
    print(f"Converted {len(rows)} profiles without changing calendar or prices.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("source")
    p.add_argument("destination", nargs="?", default="data/hackathon-dataset-anonymized.jsonl")
    a = p.parse_args()
    convert(a.source, a.destination)
