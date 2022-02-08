from pydantic import BaseModel
from typing import List, Optional
from ....client.app.api.models import GetUser

class FetchUsers(BaseModel):
    users: List[GetUser]