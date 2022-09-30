from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from enum import Enum

from app.schemas.user import UserInDb

class EnumType(str, Enum):
    ingreso = 'ingreso'
    salida = 'salida'

class BaseTransaction(BaseModel):
    count: Optional[int]
    type: Optional[EnumType]
    user_x_enterprise_id: Optional[int]

    class Config:
        use_enum_values=True

class UserXTransaction(BaseModel):
    users: UserInDb

class TransactionInDb(BaseTransaction):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    id: int
    user_x_enterprises: Optional[UserXTransaction]