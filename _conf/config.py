import socket

if socket.gethostname() in ['aly']:
    path = '/root/sync/Config/config.json'
else:
    path = r'‪E:\Sync\Config\config.json'

MYSQL_HOST = '192.168.0.27'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PWD = '123456'
MYSQL_CHARSET = "utf8"

MONGO_HOST = '192.168.0.27'
MONGO_PORT = 27017
MONGO_USER = 'root'
MONGO_PWD = '123456'

REDIS_HOST = '192.168.0.27'
REDIS_PWD = '123456'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_MAX_CONN = 999
