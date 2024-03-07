import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techcrunch_scraper.settings')
app = Celery('techcrunch_scraper')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'crawl-techcrunch-posts-every-24-hours': {
        'task': 'scraper.tasks.crawl_techcrunch_posts',
        'schedule': timedelta(hours=24),
    },
}
