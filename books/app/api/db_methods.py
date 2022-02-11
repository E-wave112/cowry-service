from .models import (
    Books,
    BorrowBooks,
    SingleBook,
    getAllBooks,
    RemoveBooks,
    FilterBooks,
)
from .db import books,engine
from typing import List

db = engine.connect()

async def add_books(payload: Books):
    query = books.insert().values(**payload.dict())

    return await db.execute(query=query)


async def get_book(id: int) -> SingleBook:
    query = books.select().where(books.b.id == id)
    sig = await db.execute(query=query)
    return sig


async def borrow_books(payload: BorrowBooks):
    query = books.update().where(books.b.id == payload.id).values(**payload.dict())
    return await db.execute(query=query)


async def get_all_books() -> List[SingleBook]:
    query = books.select()
    return await db.execute(query=query)


async def remove_books(payload: RemoveBooks):
    query = books.delete().where(books.b.id == payload.id)
    return await db.execute(query=query)


async def filter_books(payload: FilterBooks) -> List[SingleBook]:
    query = books.select().where(
        books.b.publisher == payload.publisher, books.b.category == payload.category
    )
    return await db.execute(query=query)
    # query = books.select().where(books.b.publisher==payload.publisher)
    # return await database.fetch_all(query=query)


async def get_all_available_books() -> List[SingleBook]:
    query = books.select().where(books.b.inStock == True)
    return await db.execute(query=query)


async def get_all_unavailable_books() -> List[SingleBook]:
    query = books.select().where(books.b.inStock == False)
    return await db.execute(query=query)
