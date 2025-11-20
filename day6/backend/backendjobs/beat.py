from backendjobs.worker import celery_app
from celery.schedules import crontab

celery_app.conf.beat_schedule = {
    'hello-at-a-specific-time': {
        'task': 'backendjobs.tasks.hello',
        'schedule': crontab(day_of_month='17', hour='15', minute='4'),  # At 13:38 every day
    },
    'add-at-a-specific-time': {
        'task': 'backendjobs.tasks.add',
        'schedule': crontab(day_of_month='20', hour='11', minute='4'),  # At 13:38 every day
        'args': (1, 2),
    },
}