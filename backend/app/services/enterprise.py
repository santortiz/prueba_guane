


from app.config import settings
from app.infra.services.base_service import BaseService

class EnterpriseService(BaseService):
    pass


enterprise_service = EnterpriseService(url=f"{settings.PRUEBA_DATABASE}/enterprises" )
