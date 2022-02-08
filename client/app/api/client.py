from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import GetUser,AddUser
from ....books.app.api.models import SingleBook,FetchBooks
from ....books.app.api.db_methods import get_all_available_books,get_book,borrow_books
from app.api import db_methods
from utils import date_in_string

users = APIRouter()

@users.post('/add', response_model=GetUser, status_code=201)
async def create_cast(payload: AddUser):
    user_id = await db_methods.add_users(payload)

    response = {
        'id': user_id,
        **payload.dict(),
        'created_at':date_in_string()
    }

    return response


@users.get('/books', response_model=List[SingleBook])
async def get_books():
    books = await get_all_available_books()
    return books

@users.get('/books/{id}', response_model=SingleBook)
async def get_book(id:int):
    book = await get_book(id)
    return book

#endpoint to filter books using params
@users.get('/books/filter', response_model=List[SingleBook])
async def filter_books(publisher:str,category:str):
    books = await db_methods.filter_books(publisher,category)
    return books

@users.put('/borrow/books/{id}', response_model=SingleBook)
async def borrow_book(id:int,no_of_days:int):
    book = await get_book(id)
    if book.inStock:
        await borrow_books(id,no_of_days)
        return book
    else:
        raise HTTPException(status_code=400, detail='Book is not available')
# @casts.get('/{id}/', response_model=CastOut)
# async def get_cast(id: int):
#     cast = await db_manager.get_cast(id)
#     if not cast:
#         raise HTTPException(status_code=404, detail="Cast not found")
#     return cast