from typing import List, Optional, Dict, Any

from starlette.responses import Response

from fastapi import APIRouter, Query, Depends
from fastapi.responses import JSONResponse


from app.schemas.enterprise import CreateEnterprise, EnterpriseInDb, PayloadEnterprise, UpdateEnterprise
from app.services.enterprise import enterprise_service


router = APIRouter()

@router.get(
    "",
    response_model=List[EnterpriseInDb],
    response_class=JSONResponse,
    status_code=200,
    responses= {
        200: {"description": "Enterprise found"},
        400: {"description": "Error during listing"}
    }

)
async def get_all(
    *,
    payload: PayloadEnterprise= Depends(PayloadEnterprise),
    skip: int = Query(0),
    limit: int = Query(99999)
) -> Optional[List[EnterpriseInDb]]:

    enterprises = await enterprise_service.get_all(payload=payload.dict(exclude_none=True), skip= skip, limit=limit)
    return enterprises


@router.get(
    "/{id}",
    response_model=EnterpriseInDb,
    response_class=JSONResponse,
    status_code=200,
    responses={
        200: {"description": "City found"},
        400: {"description": "Error during get by id"},
    },
)
async def get_by_id(
    *,
    id: int
) -> Optional[EnterpriseInDb]:
    """
    """
    enterprise = await enterprise_service.get_by_id(_id=id)
    return enterprise


@router.post(
    "",
    response_model= EnterpriseInDb,
    response_class=JSONResponse,
    status_code=201,
    responses= {
        201 : {"description": "Enterprise created"},
        400 : {"description": "Error during creating"}
    }
)
async def create(
    *,
    new_enterprise: CreateEnterprise
) -> Optional[EnterpriseInDb]:
    """

    """
    enterprise = await enterprise_service.create(obj_in=new_enterprise)
    return enterprise

@router.patch(
    "/{id}",
    response_model=EnterpriseInDb,
    status_code=201,
    responses={
        201: {"description": "Enterprise updated"},
        404: {"description": "Error during update"},
        404: {"description": "Object not found"},
    },
)
async def update_by_id(
    *,
    id: int,
    update_enterprise: UpdateEnterprise,
) -> Optional[EnterpriseInDb]:

    """
    """
    enterprise = await enterprise_service.update(_id=id, obj_in=update_enterprise)
    return enterprise


@router.delete(
    "/{id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "Enterprise deleted"},
        400: {"description": "Error during deleting"},
        404: {"description": "Object not found"}
    },
)
async def delete(
    *,
    id: int
) -> None:
    """
    """
    await enterprise_service.delete(_id=id)
    return Response(status_code=204)