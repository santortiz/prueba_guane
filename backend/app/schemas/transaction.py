from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseTransaction(BaseModel):
    count: Optional[int]
    type: Optional[str]
    user_x_enterprise_id: Optional[int]

class CreateTransaction(BaseTransaction):
    count: int
    type: str
    user_x_enterprise_id: int

class UpdateTransaction(BaseTransaction):
    pass

class PayloadTransaction(BaseTransaction):
    pass

class TransactionInDb(BaseTransaction):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    id: int