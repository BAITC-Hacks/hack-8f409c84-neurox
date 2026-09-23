import socket
import pytest
from app.pipeline import Engine


@pytest.fixture(autouse=True)
def offline_only(monkeypatch):
    monkeypatch.setenv("LLM_PROVIDER", "offline")
    original = socket.socket.connect
    def blocked(sock, address):
        if isinstance(address, tuple) and address[0] in ("127.0.0.1", "::1"):
            return original(sock, address)
        raise AssertionError("Network forbidden in tests")
    monkeypatch.setattr(socket.socket, "connect", blocked)


@pytest.fixture(scope="session")
def engine():
    return Engine()


@pytest.fixture
def query():
    return dict(city="Алматы", date="2026-10-01", event="свадьба", category="Фотограф", budget=1000000)
