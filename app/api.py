import os
from datetime import date
from fastapi import FastAPI, Request as HTTPRequest
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse
from dotenv import load_dotenv
from .config import ROOT
from .pipeline import Engine
from .models import Request, CompareRequest, InvalidInput
from .llm import OpenAIProvider

load_dotenv(ROOT / ".env")
provider = None
if os.getenv("LLM_PROVIDER", "offline") == "openai" and os.getenv("OPENAI_API_KEY"):
    provider = OpenAIProvider(os.environ["OPENAI_API_KEY"], os.getenv("OPENAI_MODEL", "gpt-4o-mini"))
engine = Engine(include_team=os.getenv("INCLUDE_TEAM_SYNTHETIC", "true").lower() != "false", provider=provider)
app = FastAPI(title="Alem Match", version="1.0.0", description="Умный подбор подрядчиков — HackAlem AI #79-lite")


@app.exception_handler(InvalidInput)
@app.exception_handler(RequestValidationError)
async def invalid(request: HTTPRequest, exc):
    if isinstance(exc, RequestValidationError):
        detail = "; ".join(f"{'.'.join(str(s) for s in e['loc'])}: {e['msg']}" for e in exc.errors())
    else:
        detail = str(exc)
    return JSONResponse(status_code=422, content={"status": "INVALID_INPUT", "title": "Проверьте параметры", "summary": detail, "cards": [], "allowed": engine.meta})


@app.get("/")
def index():
    return FileResponse(ROOT / "static/index.html")


@app.get("/health")
def health():
    return {"status": "ok", "profiles": len(engine.profiles), "ranking": "local-only"}


@app.get("/meta")
def meta():
    return engine.meta


@app.post("/recommend")
def recommend(query: Request):
    return engine.recommend(query)


@app.post("/compare-dates")
def compare(query: CompareRequest):
    base = Request.model_validate(query.model_dump(exclude={"second_date"}))
    return engine.compare(base, query.second_date)
