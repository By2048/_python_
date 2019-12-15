import redis
import pymysql

from DBUtils.PooledDB import PooledDB
from pymongo import MongoClient

from _conf.config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PWD, MYSQL_CHARSET
from _conf.config import MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PWD
from _conf.config import REDIS_HOST, REDIS_PORT, REDIS_PWD, REDIS_DB, REDIS_MAX_CONN

redis_conn_pool = redis.ConnectionPool(
    max_connections=REDIS_MAX_CONN, decode_responses=True,
    host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PWD,
)

mongo_client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PWD}@{MONGO_HOST}:{MONGO_PORT}", maxPoolSize=999)

mysql_conn_pool = PooledDB(
    creator=pymysql, cursorclass=pymysql.cursors.DictCursor, charset='utf8',
    host=MYSQL_HOST, port=MYSQL_PORT, user=MYSQL_USER, password=MYSQL_PWD
)
