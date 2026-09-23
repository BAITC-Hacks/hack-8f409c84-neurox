from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))
START_DATE = "2026-09-23"
END_DATE = "2026-12-31"
