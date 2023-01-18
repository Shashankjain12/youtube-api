from celery.schedules import crontab
from datetime import timedelta
from tasks import task

# Celery Beat Cron Scheduler to run the tasks every 30 seconds
task.conf.CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.search_youtube',
        'schedule': timedelta(minutes=30)
    },
}

