from .models import (
    Books,
    BorrowBooks,
    SingleBook,
    getAllBooks,
    RemoveBooks,
    FilterBooks,
)
from .db import books, database
from typing import List


async def add_books(payload: Books):
    query = books.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_book(id: int) -> SingleBook:
    query = books.select(books.id == id)
    sig = await database.fetch_one(query=query)
    print(sig)
    return sig


async def borrow_books(payload: BorrowBooks):
    query = books.update().where(books.b.id == payload.id).values(**payload.dict())
    return await database.execute(query=query)


async def get_all_books() -> List[SingleBook]:
    query = books.select()
    return await database.fetch_all(query=query)


async def remove_books(payload: RemoveBooks):
    query = books.delete().where(books.b.id == payload.id)
    return await database.execute(query=query)


async def filter_books(payload: FilterBooks) -> List[SingleBook]:
    query = books.select().where(
        books.b.publisher == payload.publisher, books.b.category == payload.category
    )
    return await database.fetch_all(query=query)
    # query = books.select().where(books.b.publisher==payload.publisher)
    # return await database.fetch_all(query=query)


async def get_all_available_books() -> List[SingleBook]:
    query = books.select().where(books.inStock == True)
    return await database.fetch_all(query=query)


async def get_all_unavailable_books() -> List[SingleBook]:
    query = books.select().where(books.inStock == False)
    return await database.fetch_all(query=query)
