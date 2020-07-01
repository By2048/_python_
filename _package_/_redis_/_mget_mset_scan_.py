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
