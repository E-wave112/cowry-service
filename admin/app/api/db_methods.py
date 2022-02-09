from .models import AddAdmin
from ....client.app.api.db import users,database as DB
from ....client.app.api.models import GetUser
from typing import List
from .db import admin,database

async def get_users() -> List[GetUser]:
    query = users.select()
    return await DB.fetch_all(query=query)

async def get_user(id:int) -> GetUser:
    query = users.select(users.c.id==id)
    return await DB.fetch_one(query=query)

async def add_admin(payload: AddAdmin):
    '''
    this methods assumes that the user is not already present in the database
    '''
    query = users.insert().values(**payload.dict())
    return await database.execute(query=query)