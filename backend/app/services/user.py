from typing import Any, Optional, Union, TypeVar

from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

from app.infra.services.base_service import BaseService
from app.schemas.user import CreateUser, UpdateUser

from app.config import settings



UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class UserService(BaseService[CreateUser, UpdateUser]):

    async def get_by_id(
        self, *, document: Union[int, str], route: Optional[str] = ""
    ) -> Any:
        url = f"{self.url}{route}/{document}"
        response = await self._client.get(url_service=url)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response
    
    async def update(
        self,
        *,
        document: Union[int, str],
        obj_in: UpdateSchemaType,
        route: Optional[str] = "",
    ) -> Any:
        url = f"{self.url}{route}/{document}"
        body = obj_in.dict(exclude_none=True)
        body = jsonable_encoder(body)
        response = await self._client.patch(url_service=url, body=body)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def delete(self, *, document: Union[int, str], route: Optional[str] = "") -> Any:
        url = f"{self.url}{route}/{document}"
        response = await self._client.delete(url_service=url)
        await self._check_codes.check_codes(response=response, delete_method=True)
        return response

user_service = UserService(url=f"{settings.PRUEBA_DATABASE}/users")