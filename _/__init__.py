import os
import re
import json
import logging
import inspect

import _._config_ as config

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s %(asctime)s.%(msecs)3d %(module)s/%(funcName)s:%(lineno)d] %(message)s',
    datefmt='%H:%M:%S'
)


# 根据本地配置文件初始化config.py中的参数
def init_config():
    if not os.path.exists(config.config_file_path):
        return

    with open(config.config_file_path, 'r') as file:
        data = json.load(file)

    if not data:
        return

    config_keys = []
    for key, value in inspect.getmembers(config):
        if re.match('[A-Z][A-Z0-9_]*[A-Z]', key):
            config_keys.append(key)

    for conf_key in config_keys:
        keys = [item.lower() for item in conf_key.split("_")]

        val = None
        for key in keys:
            val = data.get(key)

        if val:
            setattr(config, conf_key, val)


init_config()
