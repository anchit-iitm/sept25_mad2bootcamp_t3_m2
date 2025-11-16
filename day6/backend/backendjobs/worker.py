from celery import Celery, Task
from app import create_app
from config import celeryConfig
from celery.schedules import crontab


app = create_app()

class addContext(Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

celery_app = Celery(app.import_name)
celery_app.config_from_object(celeryConfig)
celery_app.Task = addContext

from backendjobs import tasks

celery_app.conf.beat_schedule = {
    'hello-every-minute': {
        'task': 'backendjobs.tasks.hello',
        'schedule': crontab(day_of_month='16', hour='13', minute='39'),  # At 13:38 every day
    },
}
