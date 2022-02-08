from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from books.app.api.models import SingleBook

class AddUser(BaseModel):
    firstName:str
    lastName:str
    email:str
    phone:str
    role:Optional[str] = 'user'
    booksBorrowed:Optional[List[SingleBook]] = []

class GetUser(AddUser):
    id:int
    created_at:str