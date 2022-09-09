from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseEnterprise(BaseModel):
    name: Optional[str]
    nit: Optional[int]

class CreateEnterprise(BaseEnterprise):
    name: str
    nit: int

class UpdateEnterprise(BaseEnterprise):
    pass

class PayloadEnterprise(BaseEnterprise):
    pass

class EnterpriseInDb(BaseEnterprise):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    id: int