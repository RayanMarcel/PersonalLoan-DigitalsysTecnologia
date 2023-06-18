import os
from celery import Celery

broker_url = os.environ.get('CELERY_BROKER_URL')

app = Celery('core')
app.conf.broker_url = broker_url
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()