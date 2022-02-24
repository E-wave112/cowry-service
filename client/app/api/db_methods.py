from .models import AddUser,GetUser
from .db import users,engine,database
from typing import Any, List,Union
from sqlalchemy import update,select

db = engine.connect()

async def add_users(payload: AddUser):
    '''
    this methods assumes that the user is not already present in the database
    '''
    query = users.insert().values(**payload.dict())
    return await database.execute(query)

async def find_user(email:str) -> GetUser:
    query = select(users).where(users.c.email==email)
    result = await database.fetch_one(query)
    return result

async def get_users() -> Union[List[GetUser],List]:
    query = select(users)
    result = await database.fetch_all(query)
    return result
    

async def get_user(id:int) -> GetUser:
    query = select(users).where(users.c.id==id)
    result = await database.fetch_one(query)
    if not result:return {"message":"Not found"}
    return result

async def get_user_by_fields(data:Any) -> GetUser:
    query = select(users).where(users.c.data==data)
    result = await database.fetch_one(query)
    if not result:return {"message":"Not found"}
    return result

async def update_user_books(id:int,book_id:int):
    user = get_user(id)
    query = update(users).where(users.c.id==user.c.id).values(booksBorrowed =user.c.booksBorrowed.append(book_id))
    await database.execute(query)
    return {"message":"user updated successfully!"}
