from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_limits_returns_a_date_for_every_device():
    body = client.get("/limits").json()
    assert body["limit"] == 100_000
    assert body["devices"] == [
        {"device_id": "DEV-A", "limit_date": "2026-06-30"},
        {"device_id": "DEV-B", "limit_date": "2026-04-01"},
        {"device_id": "DEV-C", "limit_date": "2026-01-16"},
    ]
