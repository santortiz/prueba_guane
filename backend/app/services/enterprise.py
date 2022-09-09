from app.infra.services.base_service import BaseService
from app.schemas.enterprise import CreateEnterprise, UpdateEnterprise

from app.config import settings

class EnterpriseService(BaseService[CreateEnterprise, UpdateEnterprise]):
    pass


enterprise_service = EnterpriseService(url=f"{settings.PRUEBA_DATABASE}/enterprises")
