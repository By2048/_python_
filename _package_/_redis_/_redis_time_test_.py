import logging
import random

import redis

from _tool_._decorator_ import run_time

HOST = '192.168.0.27'
PASSWORD = '123456'
MAX_CONNECTIONS = 1000
HEALTH_CHECK_INTERVAL = 30

MAX = 100_000
MAX_KEY = 10
MAC_VALUE = 100


@run_time
def get_data():
    def _random(length):
        data = [random.choice('qwertyuiopasdfghjklzxcvbnm') for _ in range(length)]
        data = ''.join(data)
        return data

    data = {}
    for i in range(MAX):
        data[_random(MAX_KEY)] = _random(MAC_VALUE)
    return data


data = get_data()


@run_time
def test_1():
    db = redis.Redis(host=HOST, password=PASSWORD)
    for key, value in data.items():
        db.set(key, value)


@run_time
def test_2():
    connection_pool = redis.ConnectionPool(
        max_connections=MAX_CONNECTIONS,
        host=HOST, password=PASSWORD
    )
    db = redis.Redis(connection_pool=connection_pool)
    for key, value in data.items():
        db.set(key, value)


@run_time
def test_4():
    db = redis.Redis(host=HOST, password=PASSWORD)
    db.mset(data)


@run_time
def flush_db():
    db = redis.Redis(host=HOST, password=PASSWORD)
    db.flushdb()


if __name__ == '__main__':
    flush_db()

    test_1()
    test_2()
    test_4()
