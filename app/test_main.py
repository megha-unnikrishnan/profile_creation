from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_valid_password():
    response = client.post("/create-profile", json={
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "password": "Secure@123"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "Profile created successfully!"

def test_weak_password():
    response = client.post("/create-profile", json={
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890",
        "password": "weakpass"
    })
    assert response.status_code == 422
    assert "Password does not meet policy requirements" in response.json()["error"]

def test_missing_password():
    response = client.post("/create-profile", json={
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "1234567890"
    })
    assert response.status_code == 422
    assert "password" in response.json()["detail"][0]["loc"]
