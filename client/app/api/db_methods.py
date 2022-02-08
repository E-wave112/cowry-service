from .models import AddUser,GetUser
from .db import users, database
from typing import List

async def add_users(payload: AddUser):
    query = users.insert().values(**payload.dict())
    return await database.execute(query=query)

async def find_user(email:str) -> GetUser:
    query = users.select(users.c.email==email)
    return await database.fetch_all(query=query)