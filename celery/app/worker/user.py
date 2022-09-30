from app.core.celery import celery_app

from app.schemas.user import UserInDb

from logging import getLogger

log = getLogger(__name__)


@celery_app.task
def notify_creation(
    obj_in: UserInDb
)-> None:
    log.info(f"Se ha creado el siguiente usuario: \n {obj_in}")

