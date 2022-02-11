from .models import AddAdmin
from .db import admin,engine

db = engine.connect()

async def add_admin(payload: AddAdmin):
    '''
    this methods assumes that the user is not already present in the database
    '''
    query = admin.insert().values(**payload.dict())
    return await db.execute(query=query)