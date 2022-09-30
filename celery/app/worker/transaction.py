from app.core.celery import celery_app

from app.schemas.transaction import TransactionInDb

from logging import getLogger
log = getLogger(__name__)

@celery_app.task
def notify_new_transaction(
    obj_in: TransactionInDb
)-> None:
    log.info(f"Recientemente se créo la siguiente transaction: \n {obj_in}")
