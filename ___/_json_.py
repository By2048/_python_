import json
import logging
from pprint import pprint, pformat

from loguru import logger as logging


class Boy(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}\t{self.age}"


def test_load_dump():
    boy = Boy('Jake', 20)

    def boy_dump(item):
        if isinstance(item, Boy):
            return {'_name': item.name, '_age': item.age}
        return item

    def boy_load(data):
        if data.get('_name') and data.get('_age'):
            return Boy(data['_name'], data['_age'])
        return data

    data = json.dumps(boy, default=boy_dump)
    logging.info(data)

    boy = json.loads(data, object_hook=boy_load)
    logging.info(boy)


if __name__ == '__main__':
    test_load_dump()
