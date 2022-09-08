from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    document: Optional[str]
    name: Optional[str]
    email: EmailStr

class CreateUser(BaseUser):
    pass

class UpdateUser(BaseUser):
    pass

class PayloadUser(BaseUser):
    pass

class UserInDb(BaseUser):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]