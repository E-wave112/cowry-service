from .models import AddUser,GetUser
from .db import users, database
from typing import List

async def add_users(payload: AddUser):
    '''
    this methods assumes that the user is not already present in the database
    '''
    query = users.insert().values(**payload.dict())
    return await database.execute(query=query)

async def find_user(email:str) -> GetUser:
    query = users.select(users.c.email==email)
    return await database.fetch_all(query=query)

async def get_users() -> List[GetUser]:
    query = users.select()
    return await database.fetch_all(query=query)

async def get_user(id:int) -> GetUser:
    query = users.select(users.c.id==id)
    return await database.fetch_one(query=query)