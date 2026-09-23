import argparse
import json
import sys
from pydantic import ValidationError
from .pipeline import Engine
from .models import InvalidInput


def main():
    parser = argparse.ArgumentParser(description="Alem Match: до трёх подрядчиков с объяснениями")
    for arg in ("city", "date", "event", "category"):
        parser.add_argument("--"+arg, required=True)
    parser.add_argument("--budget", type=int, required=True)
    parser.add_argument("--hours", type=float)
    parser.add_argument("--lang")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--no-team-synthetic", action="store_true")
    args = vars(parser.parse_args())
    output_json = args.pop("json")
    engine = Engine(include_team=not args.pop("no_team_synthetic"))
    try:
        result = engine.recommend(args)
    except (InvalidInput, ValidationError) as exc:
        result = {"status": "INVALID_INPUT", "summary": str(exc), "allowed": engine.meta, "cards": []}
    if output_json:
        print(json.dumps(result, ensure_ascii=False))
    else:
        print(result["status"], result["summary"], sep="\n")
        for card in result["cards"]:
            print(f"\n{card['anon_name']} · {card['category']} · {card['city']} · от {card['price']}")
            print(card["badge"], card["data_quality_note"])
            print(card["explanation"])
        for hint in result.get("hints", []):
            print("\nПодсказка:", hint)
        print("\nTrace:", json.dumps(result.get("trace", []), ensure_ascii=False, indent=2))
    return 2 if result["status"] == "INVALID_INPUT" else 0


if __name__ == "__main__":
    sys.exit(main())
