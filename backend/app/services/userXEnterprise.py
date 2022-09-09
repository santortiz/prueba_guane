from typing import Any, Optional, Union

from app.infra.services.base_service import BaseService
from app.schemas.userXEnterprise import CreateUserXEnterprise, UpdateUserXEnterprise

from app.config import settings

class UserXEnterpriseService(BaseService[CreateUserXEnterprise, UpdateUserXEnterprise]):
    pass

user_x_enterprise_service = UserXEnterpriseService(url=f"{settings.PRUEBA_DATABASE}/user-x-enterprises")