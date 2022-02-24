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
        "booksBorrowed": [],
        "id": 4,
        "created_at": "24-02-2022, 10:49:57",
    },
    2: {
        "firstName": "Francois",
        "lastName": "Chollet",
        "email": "francois@chollet.com",
        "phone": "+2347081927812",
        "role": "user",
        "booksBorrowed": [1,2],
        "id": 5,
        "created_at": "24-02-2022, 10:51:17",
    },
}
