from celery.schedules import crontab
from datetime import timedelta
from tasks import task

task.conf.CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.search_youtube',
        'schedule': timedelta(seconds=30)
    },
}

