import pytest
from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_endpoints(query):
    assert client.get("/").status_code == 200
    assert "alem match" in client.get("/").text
    assert client.get("/health").json()["profiles"]==66
    assert "Зарубежье" in client.get("/meta").json()["cities"]
    r = client.post("/recommend",json=query)
    assert r.status_code==200 and r.json()["status"]=="MATCHED"
    assert client.post("/compare-dates",json={**query,"second_date":"2026-10-02"}).status_code==200


@pytest.mark.parametrize("update",[{"city":"Нет"},{"category":"Нет"},{"event":"Нет"},{"lang":"Нет"},{"budget":0},{"budget":-1},{"date":"2027-01-01"},{"date":"2026-02-30"},{"hours":0},{"hours":-1},{"extra":"bad"}])
def test_invalid_input(query,update):
    r=client.post("/recommend",json={**query,**update})
    assert r.status_code==422
    assert r.json()["status"]=="INVALID_INPUT" and r.json()["summary"]
    assert "allowed" in r.json()


def test_missing_fields_and_bad_comparison(query):
    assert client.post("/recommend",json={}).status_code==422
    assert client.post("/compare-dates",json={**query,"second_date":"2027-01-01"}).status_code==422
