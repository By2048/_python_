import redis
import pymysql

from DBUtils.PooledDB import PooledDB
from pymongo import MongoClient

from _conf_._config_ import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_CHARSET
from _conf_._config_ import MONGODB_HOST, MONGODB_PORT, MONGODB_USER, MONGODB_PASSWORD, MONGODB_MAX_POOL_SIZE
from _conf_._config_ import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD, REDIS_DB, REDIS_MAX_CONNECTIONS

redis_connection_pool = redis.ConnectionPool(
    host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD,
    max_connections=REDIS_MAX_CONNECTIONS, decode_responses=True
)

mongo_client = MongoClient(
    f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}:{MONGODB_PORT}",
    maxPoolSize=MONGODB_MAX_POOL_SIZE
)

mysql_conn_pool = PooledDB(
    host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PASSWORD,
    creator=pymysql, cursorclass=pymysql.cursors.DictCursor, charset=MYSQL_CHARSET,
)
