from .models import (
    Books,
    BorrowBooks,
    SingleBook,
    getAllBooks,
    RemoveBooks,
    FilterBooks,
)
from .db import books,engine,database
from typing import List,Union
from sqlalchemy import select,delete,update
db = engine.connect()

async def add_books(payload: Books):
    query = books.insert().values(**payload.dict())
    return await database.execute(query)


async def get_book(id: int) -> Union[SingleBook,dict]:
    query = select(books).where(books.c.id == id)
    result = await database.fetch_one(query)
    if not result:return {"message":"Not found"}
    return result


async def borrow_books(payload: BorrowBooks):
    # payload_dict = dict([(k,v) for k,v in payload.items() if pay])
    payload_dict = {"id":payload["id"],"DateAvailable":payload["DateAvailable"],"inStock":payload["inStock"]}
    query = update(books).where(books.c.id == payload["id"]).values(payload_dict
    )
    return await database.execute(query)
    


async def get_all_books() -> List[SingleBook]:
    query = select(books)
    result = await database.fetch_all(query)
    return result


async def remove_books(payload: RemoveBooks):
    query = delete(books).where(books.c.id == payload["id"])
    await database.execute(query)
    return {"message":"book removed successfully"}


async def filter_books(payload: FilterBooks):
    query = select(books).where(
        books.c.publisher == payload.publisher, books.c.category == payload.category
    )
    result = await database.fetch_all(query)
    return result
    # query = books.select().where(books.b.publisher==payload.publisher)
    # return await database.fetch_all(query=query)


async def get_all_available_books() -> List:
    query = select(books).where(books.c.inStock == True)
    result = await database.fetch_all(query)
    return result


async def get_all_unavailable_books() -> List[SingleBook]:
    query = select(books).where(books.c.inStock == False)
    result = await database.fetch_all(query)
    return result
