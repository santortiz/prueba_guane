from typing import Any, Dict, Optional

from fastapi.encoders import jsonable_encoder

from app.infra.services.base_service import BaseService
from app.schemas.transaction import CreateTransaction, UpdateTransaction

from app.config import settings

class TransactionService(BaseService[CreateTransaction, UpdateTransaction]):
    
    async def create(
        self, *, obj_in: CreateTransaction, route: Optional[str] = ""
    ) -> Any:
        url = f"{self.url}{route}"
        body = jsonable_encoder(obj_in)
        response = await self._client.post(url_service=url, body=body)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

transaction_service = TransactionService(url=f"{settings.PRUEBA_DATABASE}/transactions")
