import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE','myshoppingsite.settings')

app = Celery('myshoppingsite')

app.config_from_object('django.conf:settings',namespace = 'CELERY')
app.autodiscover_tasks()