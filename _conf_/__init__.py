import os
import json
import logging

import _conf_._config_ as config

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s %(asctime)s.%(msecs)3d %(module)s/%(funcName)s:%(lineno)d] %(message)s',
    datefmt='%H:%M:%S'
)


def init_config():
    if not os.path.exists(config.path):
        return

    with open(config.path, 'r') as file:
        data = file.readlines()
        data = ''.join(data)
        data = json.loads(data)

    if not data:
        return

    config.REDIS_HOST = data.get('redis').get('host')
    config.REDIS_PORT = data.get('redis').get('port')
    config.REDIS_PASSWORD = data.get('redis').get('password')

    config.MYSQL_HOST = data.get('mysql').get('host')
    config.MYSQL_PORT = data.get('mysql').get('port')
    config.MYSQL_USER = data.get('mysql').get('user')
    config.MYSQL_PASSWORD = data.get('mysql').get('password')

    config.SSH_HOST = data.get('ssh').get('host')
    config.SSH_USER = data.get('ssh').get('user')
    config.SSH_PORT = data.get('ssh').get('port')
    config.SSH_RSA = data.get('ssh').get('rsa')
    config.SSH_PASSWORD = data.get('ssh').get('password')


init_config()
