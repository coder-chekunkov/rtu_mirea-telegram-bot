from celery import Celery
from celery.schedules import crontab
import parse_countries
import parse_news

app = Celery()
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=12),
        parse_countries.stat_create(),
    )
    sender.add_periodic_task(
        crontab(hour=2),
        parse_news.get_news()
    )