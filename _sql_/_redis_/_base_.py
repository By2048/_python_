import json
import logging

try:
    from ._config_ import connection_pool
except ImportError:
    from _config_ import connection_pool
from _tool_._logging_ import init_logging_base

import redis

init_logging_base()

db = redis.Redis(connection_pool=connection_pool)


def _set_():
    result = db.set('key|set', 'value|set', ex=None, px=None, nx=False, xx=False)
    assert result is True


def _setex_():
    result = db.setex('key|set', 200, 'value|set')
    assert result is True


def _get_():
    data = db.get('key|none')
    assert data is None

    data = db.get('key|set')
    assert data == 'value|set'


def _expire_():
    result = db.expire('key|none', 100)
    assert result is False

    db.set('key|expire', 'value|expire')
    result = db.expire('key|expire', 1000)
    assert result is True


def _exists_():
    result = db.exists('key|none')
    assert result == 0

    db.set('key|exists', 'value|exists')
    result = db.exists('key|exists')
    assert result == 1

    result = db.exists('key|none|1', 'key|none|2')
    assert result == 0

    result = db.exists('key|none|1', 'key|none|2', 'key|exists')
    assert result == 1


def _list_():
    db.delete('key3')
    db.rpush('key3', 1)
    db.rpush('key3', 2, 3, json.dumps([1, 2, 3]))
    logging.info(db.lrange('key3', 0, -1))


if __name__ == '__main__':
    _set_()
    _setex_()
    _get_()
    _expire_()
    _exists_()
