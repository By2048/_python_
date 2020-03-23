from datetime import timedelta

from celery.schedules import crontab

BROKER_URL = 'redis://:redis-password-1100@47.244.37.52:6379/0'
CELERY_RESULT_BACKEND = 'redis://:redis-password-1100@47.244.37.52:6379/0'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    '_package_._celery_._app2_._task1_',
    '_package_._celery_._app2_._task2_',
)

CELERYBEAT_SCHEDULE = {
    # 每5秒执行一次
    'add-every-30-seconds': {
        'task': '_package_._celery_._app2_._task1_.add',
        'schedule': timedelta(seconds=5),
        'args': (5, 8)
    },

    # 每天9:50执行一次
    'multiply-at-some-time': {
        'task': '_package_._celery_._app2_._task2_.multiply',
        'schedule': crontab(hour=9, minute=50),
        'args': (3, 7)
    }
}

"""

http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html

"""
