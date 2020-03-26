from time import time
import random

import redis


def test_1():
    db = redis.Redis(host='192.168.0.27', password='123456')
    for i in range(9000):
        key = [random.choice('qwertyuiopasdfghjklzxcvbnm') for _ in range(10)]
        value = [random.choice('qwertyuiopasdfghjklzxcvbnm') for _ in range(100)]

        key = ''.join(key)
        value = ''.join(value)

        db.set(key, value)


def test_2():
    connection_pool = redis.ConnectionPool(
        max_connections=1000, health_check_interval=30,
        host='192.168.0.27', password='123456')

    for i in range(9000):
        db = redis.Redis(connection_pool=connection_pool)

        key = [random.choice('qwertyuiopasdfghjklzxcvbnm') for _ in range(10)]
        value = [random.choice('qwertyuiopasdfghjklzxcvbnm') for _ in range(100)]

        key = ''.join(key)
        value = ''.join(value)

        db.set(key, value)


def test_3():
    for i in range(9000):
        db = redis.Redis(host='192.168.0.27', password='123456')

        key = [random.choice('qwertyuiopasdfghjklzxcvbnm') for _ in range(10)]
        value = [random.choice('qwertyuiopasdfghjklzxcvbnm') for _ in range(100)]

        key = ''.join(key)
        value = ''.join(value)

        db.set(key, value)


def test_4():
    db = redis.Redis(host='s71.53iq.com', password='smart.53iq.com@56iq')
    data = db.incr('Test')
    print(data)


# a = time()
# test_1()  # 4.138570308685303
# b = time()
# print(b - a)


# a = time()
# test_2()  # 6.475266933441162
# b = time()
# print(b - a)


# a = time()
# test_3()  # 9.085320711135864
# b = time()
# print(b - a)

test_4()
