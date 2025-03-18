from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_signup():
    response = client.post("/auth/signup", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}

def test_login():
    response = client.post("/auth/login", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()

