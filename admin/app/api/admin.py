from fastapi import APIRouter, HTTPException
from typing import List
from .models import FetchUsers, GetAdmin,AddAdmin
import httpx
import db_methods
from utils import date_in_string

admins = APIRouter()
CLIENT_SERVICE_URL='http://localhost:8001/api/v1/users'
BOOK_SERVICE_URL='http://localhost:8002/api/v1/books'

@admins.post('/add', response_model=GetAdmin, status_code=201)
async def create_user(payload: AddAdmin):
    admin_id = await db_methods.add_admin(payload)

    response = {
        'id': admin_id,
        **payload.dict(),
        'created_at':date_in_string()
    }

    return response

@admins.get('/user/{id}',response_model=FetchUsers,status_code=200)
async def get_user_details(id:int):
    user = await httpx.get(f"{CLIENT_SERVICE_URL}/{id}")
    return user

@admins.get('/',response_model=List[FetchUsers],status_code=200)
async def get_all_users():
    users = await httpx.get(CLIENT_SERVICE_URL)
    return users

@admins.get('/unavailable-books',status_code=200)
async def get_unavailable_books():
    books_unavailable = await httpx.get(f"{BOOK_SERVICE_URL}/unavailable")
    return books_unavailable

@admins.post('/new-book',status_code=201)
async def add_new_book(payload):
    book = await httpx.post(f"{BOOK_SERVICE_URL}/add",payload)
    return book

@admins.delete('/{id}',status_code=200)
async def remove_book(id):
    await httpx.delete(f"{BOOK_SERVICE_URL}/'delete/{id}")
    return {"message":"book deleted successfully"}