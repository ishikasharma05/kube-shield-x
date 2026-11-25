import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "security-api"))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_version():
    r = client.get("/version")
    assert r.status_code == 200
    assert r.json()["service"] == "security-api"