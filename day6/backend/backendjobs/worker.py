from celery import Celery, Task
from app import create_app
from config import celeryConfig
from celery.schedules import crontab
# celery -A backendjobs.worker.celery_app worker --loglevel=INFO

app = create_app()

class addContext(Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

celery_app = Celery(app.import_name)
celery_app.config_from_object(celeryConfig)
celery_app.Task = addContext

from backendjobs import tasks