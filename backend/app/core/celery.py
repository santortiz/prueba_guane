from celery import Celery
from celery.signals import setup_logging

from app.config import settings
from app.logging import Filter, Format

CELERY_BROKER = (
    f"amqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@"
    f"{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}//"
)

celery_config = {
    "broker_url": CELERY_BROKER,
    "result_expires": 7200
}

celery_app = Celery("worker", config_source=celery_config)

celery_app.conf.update(
    task_track_started=True, task_serializer="pickle", accept_content=["pickle", "json"]
)


@setup_logging.connect
def setup_loggers(*args, **kwargs):
    import logging

    log = logging.getLogger()

    handler = logging.StreamHandler()
    handler.setFormatter(Format())
    handler.addFilter(Filter())

    log.addHandler(handler)
    log.setLevel(logging.DEBUG)
