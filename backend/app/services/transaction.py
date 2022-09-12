from typing import Any, Dict, Optional

from app.infra.services.base_service import BaseService
from app.schemas.transaction import CreateTransaction, UpdateTransaction

from app.config import settings

class TransactionService(BaseService[CreateTransaction, UpdateTransaction]):
    pass

transaction_service = TransactionService(url=f"{settings.PRUEBA_DATABASE}/transactions")