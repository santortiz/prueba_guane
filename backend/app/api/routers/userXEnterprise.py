from typing import List, Optional, Dict, Any

from starlette.responses import Response

from fastapi import APIRouter, Query, Depends
from fastapi.responses import JSONResponse

from app.schemas.userXEnterprise import CreateUserXEnterprise, UserXEnterpriseInDb, UpdateUserXEnterprise, PayloadUserXEnterprise
from app.services.userXEnterprise import user_x_enterprise_service

router = APIRouter()


@router.get(
    "",
    response_model=List[UserXEnterpriseInDb],
    response_class=JSONResponse,
    status_code=200,
    responses= {
        200: {"description": "UserXEnterprise found"},
        400: {"description": "Error during listing"}
    }

)
async def get_all(
    *,
    payload: PayloadUserXEnterprise = Depends(PayloadUserXEnterprise),
    skip: int = Query(0),
    limit: int = Query(99999)
) -> Optional[List[UserXEnterpriseInDb]]:

    userXEnterprises = await user_x_enterprise_service.get_all(payload=payload.dict(exclude_none=True), skip= skip, limit=limit)
    return userXEnterprises


@router.post(
    "",
    response_model= UserXEnterpriseInDb,
    response_class=JSONResponse,
    status_code=201,
    responses= {
        201 : {"description": "UserXEnterprise created"},
        400 : {"description": "Error during creating"}
    }
)
async def create(
    *,
    new_user_x_enterprise: CreateUserXEnterprise
) -> Optional[UserXEnterpriseInDb]:
    """
    """
    user_x_enterprise = await user_x_enterprise_service.create(obj_in=new_user_x_enterprise)
    return user_x_enterprise


@router.patch(
    "/{id}",
    response_model=UserXEnterpriseInDb,
    status_code=201,
    responses={
        201: {"description": "User updated"},
        404: {"description": "Error during update"},
        404: {"description": "Object not found"},
    },
)
async def update_by_id(
    *,
    id: int,
    update_user: UpdateUserXEnterprise,
) -> Optional[UserXEnterpriseInDb]:
    """
    """
    user_x_enterprise = await user_x_enterprise_service.update(_id=id, obj_in=update_user)
    return user_x_enterprise

@router.delete(
    "/{id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "User deleted"},
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
    await user_x_enterprise_service.delete(_id=id)
    return Response(status_code=204)