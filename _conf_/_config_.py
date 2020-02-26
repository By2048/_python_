import socket

if socket.gethostname() in ['aly']:  # Linux
    path = '/root/sync/Config/config.json'
else:  # Windows
    path = r'E:\Sync\Config\config.json'

# ----------------------------------------------------- #

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'
MYSQL_CHARSET = "utf8"

MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017
MONGO_USER = 'root'
MONGO_PASSWORD = 'password'

# ----------------------------------------------------- #

REDIS_HOST = '127.0.0.1'
REDIS_PASSWORD = 'password'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_MAX_CONNECTIONS = 9999

# ----------------------------------------------------- #

SSH_HOST = '127.0.0.1'
SSH_USER = 'root'
SSH_PORT = 22
SSH_RSA = "rsa_file_path"
SSH_PASSWORD = 'password'

# ----------------------------------------------------- #
