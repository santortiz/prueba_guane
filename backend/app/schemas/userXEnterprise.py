from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseUserXEnterprise(BaseModel):
    user_document : Optional[int]
    enterprise_id : Optional[int]

class CreateUserXEnterprise(BaseUserXEnterprise):
    user_document : int
    enterprise_id : int

class UpdateUserXEnterprise(BaseUserXEnterprise):
    pass

class PayloadUserXEnterprise(BaseUserXEnterprise):
    pass

class UserXEnterpriseInDb(BaseUserXEnterprise):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    id: int