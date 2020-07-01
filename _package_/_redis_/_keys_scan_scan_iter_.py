try:
    from .___ import connection_pool
except ImportError:
    from ___ import connection_pool

import redis


def _keys_():
    pass


def _scan_():
    pass


def _scan_iter_():
    _keys_ = db.scan_iter(match=f'{key}:*', count=REDIS_DB_SIZE)
    keys = list(_keys_)
    values = db.mget(keys)

    if not keys:
        return

    data = {}

    for key, value in zip(keys, values):
        data[key] = value

    result = db.mset(data)

    return result


if __name__ == '__main__':
    _keys_()
    _scan_()
    _scan_iter_()
