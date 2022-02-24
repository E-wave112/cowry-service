from fastapi.testclient import TestClient
from api.utils import date_in_string
from api import client

user_client = TestClient(client)

user_db = {
    1: {
        "firstName": "Kevin",
        "lastName": "Dunn",
        "email": "kevin@dunn.com",
        "phone": "+2347081927814",
        "role": "user",
        "booksBorrowed": [1, 2],
        "id": 1,
        "created_at": "24-02-2022, 10:49:57",
    },
    2: {
        "firstName": "Francois",
        "lastName": "Chollet",
        "email": "francois@chollet.com",
        "phone": "+2347081927812",
        "role": "user",
        "booksBorrowed": [],
        "id": 2,
        "created_at": "24-02-2022, 10:51:17",
    },
}


def create_user():
    response = user_client.post(
        "/api/v1/users/add",
        json={
            "firstName": "Francois",
            "lastName": "Chollet",
            "email": "francois@chollet.com",
            "phone": "+2347081927812",
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        {
            "firstName": "Francois",
            "lastName": "Chollet",
            "email": "francois@chollet.com",
            "phone": "+2347081927812",
            "role": "user",
            "booksBorrowed": [],
            "id": 2,
            "created_at": "24-02-2022, 10:51:17",
        },
    }


def find_user():
    response = user_client.get("/api/v1/users/2")

    assert response.status_code == 200
    assert response.json() == {user_db[2]}

def get_user_not_in_db():
    response = user_client.get("/api/v1/users/45")
    assert response.status_code == 404
    assert response.json() == {"message": "Not found"}


def get_all_users():
    response = user_client.get("/api/v1/users")
    assert response.status_code == 200
    assert response.json() == {user_db}
