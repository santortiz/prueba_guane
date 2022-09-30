from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class BaseUser(BaseModel):
    document: Optional[int]
    name: Optional[str]
    email: Optional[str]

class CreateUser(BaseModel):
    document: int
    name: str
    email: str

class UserInDb(BaseUser):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]