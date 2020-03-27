import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config_path = os.path.join(BASE_DIR, '_conf_', '_config_.json')
if sys.platform == "win32":
    config_path = r'E:\Sync\Config\config.json'
elif sys.platform == "linux":
    config_path = '/root/sync/Config/config.json'
else:
    raise Exception("System Error")

# ----------------------------------------------------- #

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'password'

MYSQL_CHARSET = "utf8"

# ----------------------------------------------------- #

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_USER = 'root'
MONGODB_PASSWORD = 'password'

MONGODB_MAX_POOL_SIZE = 999
# ----------------------------------------------------- #

REDIS_HOST = '127.0.0.1'
REDIS_PASSWORD = 'password'
REDIS_PORT = 6379

REDIS_MAX_CONNECTIONS = 9999
REDIS_DB = 0

# ----------------------------------------------------- #

SSH_HOST = '127.0.0.1'
SSH_USER = 'root'
SSH_PORT = 22
SSH_RSA = "rsa_file_path"

# ----------------------------------------------------- #
