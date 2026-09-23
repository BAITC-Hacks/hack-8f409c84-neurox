@echo off
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo First launch. Installing dependencies...
    py -3 -m venv .venv
    .venv\Scripts\python.exe -m pip install -r requirements.txt
)

start "" http://127.0.0.1:8000
.venv\Scripts\python.exe -m uvicorn app.api:app --host 127.0.0.1 --port 8000

pause
