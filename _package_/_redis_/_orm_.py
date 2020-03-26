import json
import os
import importlib
from enum import Enum
from typing import Union

import redis

connection_pool = redis.ConnectionPool(
    host='47.244.37.52', port=6379, password="redis-password-1100", db=0,
    decode_responses=True,
)


class RK(object):

    def __init__(self, name, ex=None):
        self.name: str = name
        self.ex: Union[None, int] = ex

    def __bool__(self):
        return bool(self.name)

    def __str__(self):
        return self.name

    def init(self, **kwargs):
        return self.name.format(**kwargs)


class RQuery(object):

    def __init__(self, meta, package=None, model=None):
        self.meta = meta
        self.package = package
        self.model = model

    def get(self, **kwargs):
        name: str = self.meta.key
        name: str = name.format(**kwargs) if kwargs else name

        db = redis.Redis(connection_pool=connection_pool)
        data = db.get(name=name)
        data = json.loads(data)

        package = importlib.import_module(self.package)
        obj = getattr(package, self.model)()
        if getattr(obj, 'init'):
            obj.init(data)
        return obj

    def filter(self):
        pass

    def delete(self):
        """  """


class RModel(object):

    def __init__(self):
        self._key_ = self.Meta.key.format(**self.__dict__)
        self._ex_ = self.Meta.ex

    class Meta:
        key = None
        ex = None

    def to_json(self, *args, **kwargs):
        """  """

    def save(self, *args, **kwargs):
        db = redis.Redis(connection_pool=connection_pool)
        key = self._key_
        ex = self._ex_

        if self.__getattribute__('to_json'):
            value = self.to_json(*args, **kwargs)
            value = json.dumps(value, ensure_ascii=False)
        else:
            value = json.dumps(self.__dict__, ensure_ascii=False)

        db.set(key, value, ex)


class User(RModel):
    # objects = RQuery()

    def __init__(self, data=None):
        self.id: int = 0
        self.name: str = ''
        self.age: int = 0

        if data:
            self.init(data)
        super().__init__()

    class Meta:
        key = 'device:{id}'
        ex = 9999

    def init(self, data):
        self.id = data.get('id')
        self.name = data.get('name')
        self.age = data.get('age')

    def to_json(self, ):
        return {'id': self.id, 'name': self.name, 'age': self.age}

    def get(self) -> 'User':
        print(123)
        return self

    package = __file__.replace('/', '\\').replace(os.getcwd(), '') \
        .lstrip('/').lstrip('\\').rstrip('.py') \
        .replace('/', '.').replace('\\', '.')

    _class_ = importlib.import_module(package, __qualname__)

    objects = RQuery(Meta, package=package, model=__qualname__)


if __name__ == '__main__':
    user = User({'id': 1, 'name': 'am', 'age': 11})
    print(user.to_json())
    user.save()

    user: User = User.objects.get(id=1)
    print(user.id, user.name, user.age)
    print(user.to_json())
