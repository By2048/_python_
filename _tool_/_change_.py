import json
import copy
import doctest
import hashlib
import logging
from bson import ObjectId
from datetime import datetime
from enum import Enum


def json_to_json(data: dict, delete: list = None, replace: list = None,
                 copy_it: bool = False, change: bool = False) -> dict:
    """ Json数据之间进行格式转换和修改

    :param data: 传入的json数据
    :param delete: 需要删除的 key  eg: ['key1']
    :param replace: 需要替换的 key eg: [('key1', 'key2')]
    :param copy_it: 是否进行复制
    :param change: 是否进行数据格式转换    datetime->'%Y-%m-%d %H:%M:%S'    ObjectId->str(ObjectId)
    :return: 转换后的数据

    >>> json_to_json(data={'a': ['1', '2', [1, 2, 3, 4]]})
    {'a': ['1', '2', [1, 2, 3, 4]]}

    >>> json_to_json(data={'name': 123, 'time': datetime(2019, 9, 9, 10, 10, 10)}, change=True)
    {'name': 123, 'time': '2019-09-09 10:10:10'}

    >>> json_to_json(data={'name': 123, 'time': datetime(2019, 9, 9, 10, 10, 10)}, change=False)
    {'name': 123, 'time': datetime.datetime(2019, 9, 9, 10, 10, 10)}

    >>> data = {'name': 123, 'time': datetime(2019, 9, 9, 10, 10, 10)}
    >>> data_1 = json_to_json(data=data)
    >>> data_2 = json_to_json(data=data, copy_it=True)
    >>> id(data) == id(data_1) != id(data_2)
    True

    >>> json_to_json(data={'name': 123, 'time': datetime(2019, 9, 9, 10, 10, 10)}, delete=['time'])
    {'name': 123}

    >>> json_to_json(
    ...    data={'name': 123, 'time': datetime(2019, 9, 9, 10, 10, 10)},
    ...    replace=[('name', 'new_name')],
    ...    change=True
    ... )
    {'time': '2019-09-09 10:10:10', 'new_name': 123}

    """

    if not isinstance(data, dict):
        logging.error(f'传入数据错误 type:{type(data)} data:{repr(data)}')

    data = copy.deepcopy(data) if copy_it else data

    for key in list(data):
        value = data[key]
        if delete and key in delete:
            del data[key]
            continue
        if replace and key in [item[0] for item in replace]:
            keys = [item for item in replace if item[0] == key]
            old_key, key = keys[0][0], keys[0][1]
            data[key] = value
            del data[old_key]
        if isinstance(value, datetime) and change:
            data[key] = value.strftime('%Y-%m-%d %H:%M:%S')
            continue
        if isinstance(value, ObjectId) and change:
            data[key] = str(value)
            continue
        if issubclass(type(value), Enum) and change:
            data[key] = value.name
            continue
        if isinstance(value, list):
            for _value in value:
                if isinstance(_value, dict):
                    json_to_json(data=_value, delete=delete, replace=replace, change=change)
        if isinstance(value, dict):
            json_to_json(data=value, delete=delete, replace=replace, change=change)

    return data


def json_from_json(data: dict, copy_it: bool = False):
    """ 将 bson_to_json() 中转换后的数据进行还原

    :param data: 传入的json数据
    :param copy_it: 是否进行复制
    :return: 转换后的数据
    """

    def check_object_id(item: str) -> bool:
        return ObjectId.is_valid(item)

    def check_datetime(item: str) -> bool:
        """ 验证文本时间格式是否正确 """
        try:
            datetime.strptime(item, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return False
        return True

    if not isinstance(data, dict):
        logging.error(f'传入数据错误 type:{type(data)} data:{repr(data)}')

    if copy_it:
        data = copy.deepcopy(data)

    for key in list(data):
        value = data[key]
        if isinstance(value, str) and check_datetime(value):
            data[key] = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            continue
        if isinstance(value, str) and check_object_id(value):
            data[key] = ObjectId(value)
            continue
        if isinstance(value, list):
            for _value in value:
                if isinstance(_value, dict):
                    json_from_json(_value)
        if isinstance(value, dict):
            json_from_json(value)

    return data


def make_password(data: str):
    md5 = hashlib.md5()
    md5.update(data.encode())
    result = md5.hexdigest()
    return result


if __name__ == '__main__':
    doctest.testmod()
