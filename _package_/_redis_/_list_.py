import json
import logging

import redis

try:
    from .___ import connection_pool
except ImportError:
    from ___ import connection_pool
from _tool_._logging_ import init_logging_base

init_logging_base()

db = redis.Redis(connection_pool=connection_pool)


def _list_():
    db.delete('key|list')

    result = db.lpush('key|list', 'value|list|1')
    assert result == 1

    result = db.lpush('key|list', 'value|list|2')
    assert result == 2

    result = db.rpush('key|list', 'value|list|3')
    assert result == 3

    result = db.rpush('key|list', 'value|list|4', 'value|list|5')
    assert result == 5

    # 1             2             3             4             5
    # value|list|2  value|list|1  value|list|3  value|list|4  value|list|5

    result = db.lrange('key|list', 0, -1)
    assert result == ['value|list|2', 'value|list|1', 'value|list|3', 'value|list|4', 'value|list|5']
    result = db.lrange('key|list', 1, 3)
    assert result == ['value|list|1', 'value|list|3', 'value|list|4']

    result = db.lset('key|list', 2, 'value|list|333')
    assert result is True
    result = db.lrange('key|list', 0, -1)
    assert result == ['value|list|2', 'value|list|1', 'value|list|333', 'value|list|4', 'value|list|5']


if __name__ == '__main__':
    _list_()
