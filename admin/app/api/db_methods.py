from ....client.app.api.db import users,database as DB
from ....client.app.api.models import GetUser
from typing import List

async def get_users() -> List[GetUser]:
    query = users.select()
    return await DB.fetch_all(query=query)

async def get_user(id:int) -> GetUser:
    query = users.select(users.c.id==id)
    return await DB.fetch_one(query=query)