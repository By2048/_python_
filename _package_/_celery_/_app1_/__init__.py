from celery import Celery

app = Celery('_app1_')

app.config_from_object('_package_._celery_._app1_._config_')
