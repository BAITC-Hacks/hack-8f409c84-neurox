from datetime import date
from pydantic import BaseModel, ConfigDict, Field


class Request(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)
    city: str
    date: date
    event: str
    category: str
    budget: int = Field(gt=0, le=1_000_000_000)
    hours: float | None = Field(default=None, gt=0, le=1000)
    lang: str | None = None


class CompareRequest(Request):
    second_date: date


class InvalidInput(ValueError):
    pass
