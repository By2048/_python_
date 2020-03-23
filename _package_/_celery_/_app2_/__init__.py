from celery import Celery

app = Celery('_app2_')

app.config_from_object('_package_._celery_._app2_._config_')
