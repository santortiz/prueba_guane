from typing import List, Optional, Dict, Any

from starlette.responses import Response

from fastapi import APIRouter, Query, Depends
from fastapi.responses import JSONResponse


from app.schemas.transaction import CreateTransaction, TotalCount, TotalCountPayloadTransaction, TransactionInDb, PayloadTransaction, UpdateTransaction
from app.services.transaction import transaction_service


router = APIRouter()

@router.get(
    "",
    response_model=List[TransactionInDb],
    response_class=JSONResponse,
    status_code=200,
    responses= {
        200: {"description": "Transaction found"},
        400: {"description": "Error during listing"}
    }
)
async def get_all(
    *,
    payload: PayloadTransaction= Depends(PayloadTransaction),
    skip: int = Query(0),
    limit: int = Query(99999)
) -> Optional[List[TransactionInDb]]:

    transactions = await transaction_service.get_all(payload=payload.dict(exclude_none=True), skip= skip, limit=limit)
    return transactions

@router.get(
    "/totalcount",
    response_model=TotalCount,
    response_class=JSONResponse,
    status_code=200,
    responses= {
        200: {"description": "Transaction done"},
        400: {"description": "Error during listing"}
    }
)
async def get_total_count(
    *,
    payload: TotalCountPayloadTransaction= Depends(TotalCountPayloadTransaction),
    skip: int = Query(0),
    limit: int = Query(99999)
) -> Optional[TotalCount]:

    totalCount = await transaction_service.get_all(payload=payload.dict(exclude_none=True), skip= skip, limit=limit, route= '/totalcount')
    return totalCount

@router.get(
    "/{id}",
    response_model=TransactionInDb,
    response_class=JSONResponse,
    status_code=200,
    responses={
        200: {"description": "Transaction found"},
        400: {"description": "Error during get by id"},
    },
)
async def get_by_id(
    *,
    id: int
) -> Optional[TransactionInDb]:
    """
    """
    transaction = await transaction_service.get_by_id(_id=id)
    return transaction


@router.post(
    "",
    response_model= TransactionInDb,
    response_class=JSONResponse,
    status_code=201,
    responses= {
        201 : {"description": "Transaction created"},
        400 : {"description": "Error during creating"}
    }
)
async def create(
    *,
    new_transaction: CreateTransaction
) -> Optional[TransactionInDb]:
    """

    """
    transaction = await transaction_service.create(obj_in=new_transaction)
    return transaction

@router.patch(
    "/{id}",
    response_model=TransactionInDb,
    status_code=201,
    responses={
        201: {"description": "Transaction updated"},
        404: {"description": "Error during update"},
        404: {"description": "Object not found"},
    },
)
async def update_by_id(
    *,
    id: int,
    update_transaction: UpdateTransaction,
) -> Optional[TransactionInDb]:

    """
    """
    transaction = await transaction_service.update(_id=id, obj_in=update_transaction)
    return transaction


@router.delete(
    "/{id}",
    response_class=Response,
    status_code=204,
    responses={
        204: {"description": "Transaction deleted"},
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
    await transaction_service.delete(_id=id)
    return Response(status_code=204)