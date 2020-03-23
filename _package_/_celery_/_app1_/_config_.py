BROKER_URL = 'redis://:redis-password-1100@47.244.37.52:6379/0'
CELERY_RESULT_BACKEND = 'redis://:redis-password-1100@47.244.37.52:6379/0'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERY_IMPORTS = (
    '_package_._celery_._app1_._task1_',
    '_package_._celery_._app1_._task2_',
)
