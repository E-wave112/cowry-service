from pydantic import BaseModel
from typing import List, Optional
from ....client.app.api.models import GetUser

class FetchUsers(BaseModel):
    users: List[GetUser]

class AddAdmin(BaseModel):
    name:str
    email:str
    phone:str
    role:Optional[str] = 'admin'

class GetAdmin(AddAdmin):
    id:int
    created_at:str