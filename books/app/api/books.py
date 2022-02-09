from fastapi import APIRouter, HTTPException
from typing import List
from .models import SingleBook,Books
import db_methods
from utils import date_in_string

books = APIRouter()

@books.post('/add', response_model=SingleBook, status_code=201)
async def create_cast(payload: Books):
    book_id = await db_methods.add_books(payload)

    response = {
        'id': book_id,
        **payload.dict(),
        'created_at':date_in_string()
    }

    return response


@books.get('/available', response_model=List[SingleBook],status_code=200)
async def get_books():
    books = await db_methods.get_all_available_books()
    return books

@books.get('/unavailable',response_model=List[SingleBook],status_code=200)
async def get_unavailable():
    un_books = await db_methods.get_all_unavailable_books()
    return un_books

@books.get('/{id}', response_model=SingleBook)
async def get_book(id:int):
    book = await db_methods.get_book(id)
    return book

#endpoint to filter books using params
@books.get('/filter', response_model=List[SingleBook])
async def filter_books(publisher:str,category:str):
    books = await db_methods.filter_books({'publisher':publisher, 'category':category})
    return books

@books.put('/borrow/{id}', response_model=SingleBook)
async def borrow_book(id:int,no_of_days:int):
    book = await get_book(id)
    if book.inStock:
        await db_methods.borrow_books({'id':id,'no_of_days':no_of_days})
        return book
    else:
        raise HTTPException(status_code=400, detail='Book is not available')

@books.delete('delete/{id}',status_code=200)
async def delete_book(id:int):
    await db_methods.remove_books({'id':id})