try:
    from .___ import connection_pool
except ImportError:
    from ___ import connection_pool

import redis

db = redis.Redis(connection_pool=connection_pool)


def _expire_():
    result = db.expire('key|none', 100)
    assert result is False

    db.set('key|expire', 'value|expire')
    result = db.expire('key|expire', 1000)
    assert result is True


def _exists_():
    result = db.exists('key|none')
    assert result == 0

    db.set('key|exists|1', 'value|exists|1')
    db.set('key|exists|2', 'value|exists|2')

    result = db.exists('key|exists')
    assert result == 1

    result = db.exists('key|none|1', 'key|none|2')
    assert result == 0

    result = db.exists('key|exists|1', 'key|exists|2', 'key|none')
    assert result == 2


def _delete_():
    result = db.delete('key|none')
    assert result == 0

    db.set('key|delete', 'value|delete')
    result = db.delete('key|delete')
    assert result == 1

    db.set('key|delete|1', 'value|delete|1')
    db.set('key|delete|2', 'value|delete|1')

    result = db.delete('key|none|1', 'key|none|2')
    assert result == 0

    result = db.delete('key|delete|1', 'key|delete|2', 'key|none')
    assert result == 2


if __name__ == '__main__':
    _expire_()
    _exists_()
    _delete_()
