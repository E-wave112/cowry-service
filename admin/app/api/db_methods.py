from .models import AddAdmin
# from ....client.app.api.db import users,database as DB
# from ....client.app.api.models import GetUser
from typing import List,Any
from .db import admin,database

async def add_admin(payload: AddAdmin):
    '''
    this methods assumes that the user is not already present in the database
    '''
    query = admin.insert().values(**payload.dict())
    return await database.execute(query=query)