from celery import Celery

from clients import BROKER_URL

task = Celery('tasks', broker=BROKER_URL)

@task.task(name='tasks.search_youtube')
def search_youtube():
    print('run my function')
