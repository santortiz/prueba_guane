from typing import List, Optional, Dict, Any

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from app.schemas.enterprise import CreateEnterprise, EnterpriseInDb
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
async def get_all( #por el momento no tiene payload porque no entran query parameters
    *,
    payload: Optional[Dict[str, Any]] = None,
    skip: int = Query(0),
    limit: int = Query(99999)
) -> Optional[List[EnterpriseInDb]]:

    enterprises = await enterprise_service.get_all(payload=payload, skip= skip, limit=limit)
    return enterprises


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