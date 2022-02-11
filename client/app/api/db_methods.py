from .models import AddUser,GetUser
from .db import users,engine
from typing import List

db = engine.connect()

async def add_users(payload: AddUser):
    '''
    this methods assumes that the user is not already present in the database
    '''
    query = users.insert().values(**payload.dict())
    return await db.execute(query=query)

async def find_user(email:str) -> GetUser:
    query = users.select().where(users.u.email==email)
    return await db.execute(query=query)

async def get_users() -> List[GetUser]:
    query = users.select()
    return await db.execute(query=query)

async def get_user(id:int) -> GetUser:
    query = users.select().where(users.u.id==id)
    return await db.execute(query=query)