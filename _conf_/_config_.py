import socket

if socket.gethostname() in ['aly']:  # Linux
    path = '/root/sync/Config/config.json'
else:  # Win
    path = r'‪E:\Sync\Config\config.json'

MYSQL_HOST = '192.168.0.27'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_CHARSET = "utf8"

MONGO_HOST = '192.168.0.27'
MONGO_PORT = 27017
MONGO_USER = 'root'
MONGO_PWD = '123456'

# ----------------------------------------------------- #


REDIS_HOST = '192.168.0.77'
REDIS_PASSWORD = 'docker-redis-password'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_MAX_CONNECTIONS = 9999

# ----------------------------------------------------- #
