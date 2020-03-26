import json
import logging

try:
    from ._config_ import connection_pool
except ImportError:
    from _config_ import connection_pool
from _tool_._logging_ import init_logging_base

import redis

init_logging_base()


def device_offline():
    """ 项目启动时重置设备在线状态(只有正式环境才执行) """

    db = redis.Redis(connection_pool=connection_pool)

    _keys_ = db.scan_iter(match=f'{key}:*', count=REDIS_DB_SIZE)
    keys = list(_keys_)
    values = db.mget(keys)

    if not keys:
        return

    data = {}
    for key in keys:
        data[key] = None

    for key, value in zip(keys, values):
        try:
            value = json.loads(value)
        except JSONDecodeError:
            continue
        if isinstance(value, dict):
            value['online'] = False
        value = json.dumps(value, ensure_ascii=False)
        data[key] = value

    result = db.mset(data)

    return result
