from typing import List, Optional, Dict, Any

from starlette.responses import Response

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.schemas.user import CreateUser, UserInDb, UpdateUser
from app.services.user import user_service

router = APIRouter()

@router.get(
    "",
    response_model=List[UserInDb],
    response_class=JSONResponse,
    status_code=200,
    responses= {
        200: {"description": "User found"},
        400: {"description": "Error during listing"}
    }

)
async def get_all(
    *,
    payload: Optional[Dict[str, Any]] = None,
    skip: int = Query(0),
    limit: int = Query(99999)
) -> Optional[List[UserInDb]]:

    users = await user_service.get_all(payload=payload, skip= skip, limit=limit)
    return users


@router.get(
    "/{document}",
    response_model=UserInDb,
    response_class=JSONResponse,
    status_code=200,
    responses={
        200: {"description": "User found"},
        400: {"description": "Error during get by id"},
    },
)
async def get_by_id(
    *,
    document: int
) -> Optional[UserInDb]:
    """
    """
    user = await user_service.get_by_id(document=document)
    return user

@router.post(
    "",
    response_model= UserInDb,
    response_class=JSONResponse,
    status_code=201,
    responses= {
        201 : {"description": "User created"},
        400 : {"description": "Error during creating"}
    }
)
async def create(
    *,
    new_user: CreateUser
) -> Optional[UserInDb]:
    """
    """
    user = await user_service.create(obj_in=new_user)
    return user

@router.patch(
    "/{id}",
    response_model=UserInDb,
    status_code=201,
    responses={
        201: {"description": "User updated"},
        404: {"description": "Error during update"},
        404: {"description": "Object not found"},
    },
)
async def update_by_id(
    *,
    document: int,
    update_user: UpdateUser,
) -> Optional[UserInDb]:
    """
    """
    user = await user_service.update(document=document, obj_in=update_user)
    return user


@router.delete(
    "/{document}",
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
    document: int
) -> None:
    """
    """
    await user_service.delete(document=document)
    return Response(status_code=204)