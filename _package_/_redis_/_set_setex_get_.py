import json
import logging

try:
    from .___ import connection_pool
except ImportError:
    from ___ import connection_pool
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


if __name__ == '__main__':
    _set_()
    _setex_()
    _get_()
