import json
from datetime import date
from pydantic import BaseModel, ConfigDict, Field
from .config import ROOT, START_DATE, END_DATE


class Profile(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str
    anon_name: str
    categories: list[str] = Field(min_length=1)
    city: str
    price_from_kzt: int | None = Field(default=None, ge=0)
    event_formats: list[str]
    languages: list[str]
    max_hours: float | None = Field(default=None, gt=0)
    busy_dates: list[date]
    description: str
    synthetic: bool = False
    city_imputed: bool = False
    price_imputed: bool = False
    source: str = "dataset"


def load_profiles(include_team=True, path=None):
    paths = [path or ROOT / "data/hackathon-dataset-anonymized.jsonl"]
    team = ROOT / "data/team_synthetic.jsonl"
    if include_team and team.exists():
        paths.append(team)
    result = []
    for current in paths:
        for line in current.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            p = Profile.model_validate_json(line)
            if current == team and (not p.synthetic or p.source != "team"):
                raise ValueError("Team profiles require synthetic=true and source=team")
            if any(str(d) < START_DATE or str(d) > END_DATE for d in p.busy_dates):
                raise ValueError(f"Calendar outside supported window: {p.id}")
            if any(existing.id == p.id for existing in result):
                raise ValueError(f"Duplicate profile id: {p.id}")
            result.append(p)
    return sorted(result, key=lambda p: p.id)


def read_cache(name):
    path = ROOT / "data" / name
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
