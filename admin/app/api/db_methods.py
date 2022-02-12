from .models import AddAdmin
from .db import admin,engine,database

async def add_admin(payload: AddAdmin):
    '''
    this methods assumes that the user is not already present in the database
    '''
    query = admin.insert().values(**payload.dict())
    return await database.execute(query)