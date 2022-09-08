from typing import Any, Dict, List, Optional, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic.main import BaseModel

from app.infra.httpx.client import client
from app.infra.services.base import IServiceBase
from app.infra.services.responses import Responses

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseService(IServiceBase[CreateSchemaType, UpdateSchemaType]):
    def __init__(
        self,
        url: str,
        check_codes: Responses = Responses(),
    ):
        self.url = url
        self._client = client
        self._check_codes = check_codes

    async def create(
        self, *, obj_in: CreateSchemaType, route: Optional[str] = ""
    ) -> Any:
        url = f"{self.url}{route}"
        body = jsonable_encoder(obj_in)
        response = await self._client.post(url_service=url, body=body)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def update(
        self,
        *,
        _id: Union[int, str],
        obj_in: UpdateSchemaType,
        route: Optional[str] = "",
    ) -> Any:
        url = f"{self.url}{route}/{_id}"
        body = obj_in.dict(exclude_none=True)
        body = jsonable_encoder(body)
        response = await self._client.patch(url_service=url, body=body)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def delete(self, *, _id: Union[int, str], route: Optional[str] = "") -> Any:
        url = f"{self.url}{route}/{_id}"
        response = await self._client.delete(url_service=url)
        await self._check_codes.check_codes(response=response, delete_method=True)
        return response

    async def get_by_id(
        self, *, _id: Union[int, str], route: Optional[str] = ""
    ) -> Any:
        url = f"{self.url}{route}/{_id}"
        response = await self._client.get(url_service=url)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def get_all(
        self,
        payload: Optional[Dict[str, Any]],
        skip: int = 0,
        limit: int = 99999,
        route: Optional[str] = "",
    ) -> Any:
        if payload:
            payload.update({"skip": skip, "limit": limit})
        else:
            payload = {"skip": skip, "limit": limit}
        url = f"{self.url}{route}"
        response = await self._client.get(url_service=url, params=payload)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def create_multiple(
        self, *, data: List[CreateSchemaType], route: Optional[str] = "/multiple"
    ):
        if not data:
            return []
        body = jsonable_encoder(data)
        url = f"{self.url}{route}"
        response = await self._client.post(url_service=url, body=body)
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response

    async def get_multiple_by_attribute(
        self,
        *,
        data: List[Union[int, str]],
        attribute: str = "",
        route: Optional[str] = "/multiple",
    ):
        body = jsonable_encoder(data)
        url = f"{self.url}{route}/{attribute}"
        response = await self._client.get(url_service=url, params={"codes": body})
        await self._check_codes.check_codes(response=response)
        response = response.json()
        return response
