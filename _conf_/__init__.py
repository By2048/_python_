import inspect
import os
import json
import logging
import re

import _conf_._config_ as config

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s %(asctime)s.%(msecs)3d %(module)s/%(funcName)s:%(lineno)d] %(message)s',
    datefmt='%H:%M:%S'
)


def init_config():
    if not os.path.exists(config.config_path):
        return

    with open(config.config_path, 'r') as file:
        data = file.readlines()
        data = ''.join(data)
        data = json.loads(data)

    if not data:
        return

    configs = []
    for name, obj in inspect.getmembers(config):
        if re.match('[A-Z][A-Z0-9_]*[A-Z]', name):
            configs.append(name)

    for conf in configs:
        keys = [item.lower() for item in conf.split("_")]

        val = None
        for key in keys:
            if not val:
                val = data.get(key)
            else:
                val = val.get(key)

        if val:
            setattr(config, conf, val)


init_config()
