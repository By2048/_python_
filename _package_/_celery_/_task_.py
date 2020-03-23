import time

from celery import Celery

broker = 'redis://:redis-password-1100@47.244.37.52:6379/0'
backend = 'redis://:redis-password-1100@47.244.37.52:6379/0'

app = Celery('task-test', broker=broker, backend=backend)


@app.task
def add(x, y):
    time.sleep(5)
    z = x + y
    print(x, y, z)
    return z
