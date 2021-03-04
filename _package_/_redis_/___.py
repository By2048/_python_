import redis

from _._config_ import \
    REDIS_HOST, \
    REDIS_PORT, \
    REDIS_DB, \
    REDIS_MAX_CONNECTIONS, \
    REDIS_PASSWORD

connection_pool = redis.ConnectionPool(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    db=REDIS_DB,
    decode_responses=True,
    max_connections=REDIS_MAX_CONNECTIONS,
    socket_keepalive_options=True
)
