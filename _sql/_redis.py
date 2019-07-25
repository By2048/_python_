import json
import logging

from _conf.server import redis_conn_pool

import redis

db = redis.Redis(connection_pool=redis_conn_pool, decode_responses=True)


def _set():
    db.set('key1', 'qwer1234', ex=None, px=None, nx=False, xx=False)
    db.expire('key1', 100)
    db.setex('key2', 100, 'qwer1234')


def _get():
    logging.info(db.get('key1'))

    for key in db.keys('key*'):
        key = key.decode() if isinstance(key, bytes) else key
        value = db.get(key)
        logging.info(f"{key} -> {value}")


def _list():
    db.delete('key3')
    db.rpush('key3', 1)
    db.rpush('key3', 2, 3, json.dumps([1, 2, 3]))

    logging.info(db.lrange('key3', 0, -1))


if __name__ == '__main__':
    # _set()
    # _get()
    _list()
