from pydantic import BaseModel
from typing import Any, List, Optional
# from ....client.app.api.models import GetUser

class FetchUsers(BaseModel):
    users: List[Any]

class AddAdmin(BaseModel):
    name:str
    email:str

class GetAdmin(AddAdmin):
    id:int
    created_at:str

class Books(BaseModel):
    title: str
    publisher: str
    description: Optional[str]
    category: str
    datePublished: str
    authors: Optional[List[str]]
    inStock: Optional[bool]
    DateAvailable: Optional[str]