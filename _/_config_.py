import os
import sys

# 使用配置文件中的参数覆盖此文件中的参数
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_file_path = os.path.join(BASE_DIR, '_', '_config_.json')
if sys.platform == "win32" and os.path.isfile(r'E:\Sync\Config\config.json'):
    config_file_path = r'E:\Sync\Config\config.json'
if sys.platform == "linux" and os.path.isfile(r'/root/sync/Config/config.json'):
    config_file_path = r'/root/sync/Config/config.json'

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
QQMAIL_HOST = "smtp.qq.com"
QQMAIL_PORT = 465
QQMAIL_USER = "124xxxx575@qq.com"
QQMAIL_PASSWORD = "pmbyxxxxxxxxifig"
# ----------------------------------------------------- #

BOOL_ARGS = {
    'true': True, 'True': True, 'TRUE': True, '1': True, 1: True,
    'false': False, 'False': False, 'FALSE': False, '0': False, 0: False
}
