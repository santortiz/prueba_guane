from asyncio import run
from app.core.celery import celery_app

from app.schemas.transaction import TransactionInDb, UpdateTransaction
from app.services.transaction import transaction_service

from logging import getLogger
log = getLogger(__name__)

@celery_app.task
def notify_new_transaction()-> None:
    log.info("entró")
    not_notificated_transactions = run(transaction_service.get_all(payload={"notificated": False}))

    for transaction in not_notificated_transactions:
        log.info(f"Transaction: \n {transaction}")
        run(
            transaction_service.update(
                _id=transaction["id"],
                obj_in= UpdateTransaction(notificated=True)
            )
        )
        

