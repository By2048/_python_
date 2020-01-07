import os
import json
import logging

import _conf._config as config
 
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s %(asctime)s.%(msecs)3d %(module)s/%(funcName)s:%(lineno)d] %(message)s',
    datefmt='%H:%M:%S'
)

env = os.environ.get('env') or 'aly'


def init_config():
    if not os.path.exists(config.path):
        return

    with open(config.path, 'r') as file:
        data = file.readlines()
        data = ''.join(data)
        data = json.loads(data)

    if not data:
        return

    config.REDIS_HOST = data.get(env).get('redis').get('host')
    config.REDIS_PORT = data.get(env).get('redis').get('port')
    config.REDIS_PWD = data.get(env).get('redis').get('pwd')

    config.MYSQL_HOST = data.get(env).get('mysql').get('host')
    config.MYSQL_PORT = data.get(env).get('mysql').get('port')
    config.MYSQL_USER = data.get(env).get('mysql').get('user')
    config.MYSQL_PWD = data.get(env).get('mysql').get('pwd')


init_config()
