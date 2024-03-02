import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techcrunch_scraper.settings')

app = Celery('techcrunch_scraper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
