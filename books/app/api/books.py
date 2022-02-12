from fastapi import APIRouter, HTTPException,Query
from typing import List,Optional,Union
from .models import SingleBook,Books
from .db_methods import *
from .utils import date_in_string,add_days
from datetime import date

books = APIRouter()

@books.post('/add', response_model=SingleBook, status_code=201)
async def create_cast(payload: Books):
    book_id = await add_books(payload)

    response = {
        'id': book_id,
        **payload.dict(),
        'created_at':date_in_string()
    }

    return response


@books.get('/available',status_code=200)
async def get_books():
    books = await get_all_available_books()
    return books

@books.get('/unavailable',response_model=List[SingleBook],status_code=200)
async def get_unavailable():
    un_books = await get_all_unavailable_books()
    return un_books

@books.get('/{id}', response_model=Union[SingleBook, dict])
async def get_book_single(id:int):
    book = await get_book(id)
    return book

#endpoint to filter books using params
@books.get('/filter', response_model=List[SingleBook])
async def filter_books(publisher:Optional[str]="",category:Optional[str]=""):
    books = await filter_books({'publisher':publisher, 'category':category})
    return books

@books.put('/borrow/{id}', response_model=SingleBook)
async def borrow_book(id:int, no_of_days:int, DateAvailable:Optional[str]=""):
    book = await get_book(id)
    borrowed_date:date = date.today()
    DateAvailable = add_days(borrowed_date, no_of_days)
    if book.inStock:
        await borrow_books({'id':id,'no_of_days':no_of_days,"DateAvailable":DateAvailable,"inStock":False})
        return book, {"message":"book borrowed successfully"}
    else:
        raise HTTPException(status_code=400, detail='Book is not available')

@books.delete('/delete/{id}',status_code=200)
async def delete_book(id:int):
    await remove_books({'id':id})
    return {"message":"book removed successfully"}

@books.get('/',status_code=200)
async def get_books():
    return await get_all_books()
