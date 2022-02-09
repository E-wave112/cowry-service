from fastapi import APIRouter, HTTPException
from typing import List
import httpx

BOOK_SERVICE_URL='http://localhost:8002/api/v1/books'
from app.api.models import GetUser,AddUser
from ....books.app.api.models import SingleBook
from ....books.app.api.db_methods import get_all_available_books,get_book,borrow_books
from app.api import db_methods
from utils import date_in_string

users = APIRouter()

@users.post('/add', response_model=GetUser, status_code=201)
async def create_user(payload: AddUser):
    user_id = await db_methods.add_users(payload)

    response = {
        'id': user_id,
        **payload.dict(),
        'created_at':date_in_string()
    }

    return response


@users.get('/books', response_model=List[SingleBook])
async def get_books():
    books = await httpx.get(f"{BOOK_SERVICE_URL}/available")
    return books

@users.get('/books/{id}', response_model=SingleBook)
async def get_books(id:int):
    # book = await get_book(id)
    book = await httpx.get(f"{BOOK_SERVICE_URL}/{id}")
    return book

#endpoint to filter books using params
@users.get('/books/filter', response_model=List[SingleBook])
async def filter_books(publisher:str,category:str):
    # books = await db_methods.filter_books(publisher,category)
    books = await httpx.get(f"{BOOK_SERVICE_URL}/filter",params = {'publisher': publisher, 'category': category})
    return books

@users.put('/borrow/books/{id}', response_model=SingleBook)
async def borrow_book(id:int,no_of_days:int):
    book = await get_books(id)
    if book.inStock:
        await httpx.put(f"{BOOK_SERVICE_URL}/borrow/{id}",data= {'id':id,'no_of_days':no_of_days})
        # await borrow_books(id,no_of_days)
        return book
    else:
        raise HTTPException(status_code=400, detail='Book is not available')


@users.get('/{id}',response_model=GetUser)
async def get_single_user(id:int):
    single_user = await db_methods.get_user(id)
    return single_user

@users.get('/',response_model=List[GetUser])
async def all_users():
    all_reg_users = await db_methods.get_users()
    return all_reg_users
