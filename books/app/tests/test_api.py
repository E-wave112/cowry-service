from fastapi.testclient import TestClient
from api.utils import date_in_string
from api import books


client = TestClient(books)

books_db = {
    1: {
        "id": 1,
        "title": "Origin",
        "description": "There goes my hero in Langdon",
        "publisher": "Oreilly",
        "category": "Thriller",
        "inStock": True,
        "authors": ["Dan Brown", "Richard Avici"],
        "DateAvailable": "",
        "created_at": date_in_string(),
    },
    2: {
        "id": 2,
        "title": "Space Force",
        "description": "Go to mars with SpaceX",
        "publisher": "Oreilly",
        "category": "Thriller",
        "inStock": False,
        "authors": ["Richard BrandSon", "Jordan Atkinson"],
        "DateAvailable": "",
        "created_at": date_in_string(),
    },
}


def test_single_book():
    response = client.get("/api/v1/books/1")
    assert response.status_code == 200
    assert response.json() == {books_db[1]}


def get_all_books():
    response = client.get("/api/v1/books")
    assert response.status_code == 200
    assert response.json() == {books_db}


def get_book_not_in_db():
    response = client.get("/api/v1/books/45")
    assert response.status_code == 404
    assert response.json() == {"message": "Not found"}


def create_book():
    response = client.post(
        "/api/v1/books/add",
        json={
            "title": "Welcome to OSCA",
            "description": "The largest tech conferences in lagos",
            "publisher": "Menlo Press",
            "category": "Tech",
            "inStock": True,
            "authors": ["Sheldon Cooper"],
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        {
            "id": 3,
            "title": "Welcome to OSCA",
            "description": "The largest tech conferences in lagos",
            "publisher": "Menlo Press",
            "category": "Tech",
            "inStock": True,
            "authors": ["Sheldon Cooper"],
            "created_at":date_in_string()
        }
    }


def delete_books():
    response = client.delete("api/v1/books/delete/2")
    del books_db[2]
    assert response.status_code == 200
    assert response.json() == {{"message": "book removed successfully"}}
