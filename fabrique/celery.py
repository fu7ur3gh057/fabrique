from __future__ import absolute_import

import os
from celery.schedules import crontab

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fabrique.settings')
app = Celery('fabrique')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every_minute': {
        'task': 'send_messages_task',
        'schedule': crontab()
    },
    'every_two_minute': {
        'task': 'retry_send_error_messages_task',
        'schedule': crontab(minute='*/2')
    }
}
