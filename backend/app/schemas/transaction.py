from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from enum import Enum

class EnumType(str, Enum):
    ingreso = 'ingreso'
    salida = 'salida'

class BaseTransaction(BaseModel):
    count: Optional[int]
    type: Optional[EnumType]
    user_x_enterprise_id: Optional[int]

    class Config:
        use_enum_values=True

class CreateTransaction(BaseTransaction):
    count: int
    type: str
    user_x_enterprise_id: int

class UpdateTransaction(BaseTransaction):
    pass

class PayloadTransaction(BaseTransaction):
    user_document : Optional[int]
    enterprise_id: Optional[int]

class TotalCountPayloadTransaction(BaseModel):
    user_document: int
    enterprise_id: int

class TransactionInDb(BaseTransaction):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    id: int

class TotalCount(BaseModel):
    totalCount: int