import os
import json
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

default_config_path = os.path.join(path, '_conf_', '_config_.json')

if sys.platform == "win32":
    config_path = r'E:\Sync\Config\config.json'
elif sys.platform == "linux":
    config_path = '/root/sync/Config/config.json'
else:
    raise Exception("System Error")


def remove_value(data):
    for key in list(data):
        value = data[key]
        if isinstance(value, (str, int)):
            data[key] = type(value)()
        if isinstance(value, list):
            for _value_ in value:
                if isinstance(_value_, dict):
                    remove_value(_value_)
        if isinstance(value, dict):
            remove_value(value)
    return data


def remove():
    with open(config_path, 'r') as file_system:
        data = file_system.readlines()
        data = ''.join(data)
        data = json.loads(data)
        data = remove_value(data)
        data = json.dumps(data, ensure_ascii=False, indent=4)
        with open(default_config_path, 'w') as file_default:
            file_default.writelines(data)


if __name__ == '__main__':
    remove()
