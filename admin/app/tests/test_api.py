from fastapi.testclient import TestClient
from api.utils import date_in_string
from api import admin

client = TestClient(admin)

def create_admin():
    response = client.post(
        "/api/v1/admins/add",
        json={
        "name": "Edmond Kirsch",
        "email": "edmond@kirsch.com",
    }
    )
    assert response.status_code == 201
    assert response.json() == {
        {
            "id": 1,
            "name": "Edmond Kirsch",
            "role":"admin",
            "email":"edmond@kirsch.com",
            "created_at":date_in_string()
        }
    }
