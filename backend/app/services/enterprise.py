
from app.infra.services.base_service import BaseService

from app.config import settings
from app.schemas.enterprise import CreateEnterprise, UpdateEnterprise

class EnterpriseService(BaseService[CreateEnterprise, UpdateEnterprise]):
    pass


enterprise_service = EnterpriseService(url=f"{settings.PRUEBA_DATABASE}/enterprises")
