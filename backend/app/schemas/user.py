from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    document: Optional[int]
    name: Optional[str]
    email: Optional[EmailStr]

class CreateUser(BaseUser):
    document: int
    name: str
    email: EmailStr

class UpdateUser(BaseUser):
    pass

class PayloadUser(BaseUser):
    enterprise_id: Optional[int]

class UserInDb(BaseUser):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]