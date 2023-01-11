# Python
import os

# Django
from django.conf import settings

# Local
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.base')

app = Celery('settings')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.beat_schedule = {
    'every-10-minutes-every-day': {
        'task': 'check_state_of_bookings',
        'schedule': crontab(minute='*/10')
    }
}
