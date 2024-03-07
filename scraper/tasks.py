from celery import shared_task

from scraper.models import Post
from scraper.techcrunch_crawler import TechCrunchCrawler


@shared_task
def crawl_techcrunch_posts():
    TechCrunchCrawler().get_posts()
