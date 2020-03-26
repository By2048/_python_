import time
import random

import redis
from rediscluster import RedisCluster
from rediscluster.connection import ClusterConnectionPool


# https://github.com/Grokzen/redis-py-cluster

def test_1():
    startup_nodes = [
        {'host': '192.168.0.27', 'port': '6001'},
        {'host': '192.168.0.27', 'port': '6002'},
        {'host': '192.168.0.27', 'port': '6003'},
    ]
    db = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, password='123456789')

    for i in range(50):
        db.set(f"key_{i}", i)


def test_2():
    db = redis.Redis(host='192.168.0.27', password='123456')
    for i in range(50000):
        db.set(f"key_{i}", i)


if __name__ == '__main__':
    test_1()
    test_2()
