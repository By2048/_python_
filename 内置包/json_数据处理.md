[参考blog连接](https://my.oschina.net/pangyangyang/blog/200329)

## Json 数据基础操作
`dumps`是将`dict`转化成`str`格式，`loads`是将`str`转化成`dict`格式。
`dump`和`load`也是类似的功能，只是与文件操作结合起来了。

`loads`针对内存对象
`load`针对文件句柄

```py
import json

data_dict = {
    'id': 1,
    'name': ['name_1'],
    'url': 'http://www.qwer.com'
}

print(data_dict, type(data_dict))
# {'url': 'http://www.qwer.com', 'name': ['name_1'], 'id': 1} <class 'dict'>

data_str = json.dumps(data_dict)
print(data_str, type(data_str))
# {"id": 1, "name": ["name_1"], "url": "http://www.qwer.com"} <class 'str'>

data_json = json.loads(data_str)
print(data_json, type(data_json))
# {'id': 1, 'name': ['name_1'], 'url': 'http://www.qwer.com'} <class 'dict'>

print(data_json['name'], type(data_json['name']))
# ['name_1'] <class 'list'>
print(data_json['url'], type(data_json['url']))
# http://www.qwer.com <class 'str'>

data_json['name'] += ['name_2']
print(data_json['name'], type(data_json['name']))
# ['name_1', 'name_2'] <class 'list'>

data_json['age'] = 20
print(data_json['age'], type(data_json['age']))
# 20 <class 'int'>
```



## Json 文件处理
```py
import json

# Writing JSON
with open('data.json', 'w') as file:
    json.dump(data, file)

# Reading JSON
with open('data.json', 'r') as file:
    json_data = json.load(file)
```


## 对应关系
|                   |            |
|   -------------   |   ------   |
|   JSON            |   Python   |
|   Object          |   dict     |
|   Array           |   list     |
|   String          |   str      |
|   number (int)    |   int      |
|   number (real)   |   float    |
|   true            |   True     |
|   false           |   False    |
|   null            |   None     |


## 序列化函数dumps的几个常用参数： 
```py
import json

data_dict = {
    'id': 1,
    'name': ['name_1', 'name_2'],
    'url': 'http://www.qwer.com'
}

# separators: 指定生成的json字符串所用的分隔符，两个分别用于代替“,”、“:”。
# 如果想保持原样，可以写成separators=(', ', ': ')。
# indent:     用于格式化生成的json字符串，接受整数参数的缩进量。
# sort_key:   true/false，指定dict在序列化时是否按照key排序a-z）输出。
json_info = json.dumps(data_dict, sort_keys=True, indent=4, separators=(',', '->'))

print(type(json_info))
# <class 'str'>

print(json_info)
# {
#     "id"->1,
#     "name"->[
#         "name_1",
#         "name_2"
#     ],
#     "url"->"http://www.qwer.com"
# }
```


## 自定义类型的序列化 使用函数

`json.dumps`函数接受参数`default`用于指定一个函数
该函数能够把自定义类型的对象转换成可序列化的基本类型 

`json.loads`函数接受参数`objecthook`用于指定函数
该函数负责吧反序列化后的基本类型对象转换成自定义类型的对象。
```py
import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User('Jake', 20)

# default method for decode
def user_default(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age}
    return obj

def user_hook(dic):
    if dic['name']:
        return User(dic['name'], dic['age'])
    return dic

user_encode_str = json.dumps(user1, default=user_default)
new_user = json.loads(user_encode_str, object_hook=user_hook)

print(user_encode_str)
# {"name": "Jake", "age": 20}

print(str(new_user.name), str(new_user.age), sep=' -> ')
# Jake -> 20
```



## 自定义类型的序列化 使用类

`json`库提供了`JSONEncoder`和`JSONDecoder`两个类用于`json`的序列化和反序列化
可以通过子类实现自定义类的`json`操作
`json.JSONEncoder`的主要方法：
`default`：目的和`dumps`的`default`参数一样。
`encode`：实现序列化的逻辑部分。
`json.JSONDecoder`的方法就是`decode`  
这里有两个思路一个是重载`Decoder`的构造函数设置`object_hook`，另一个是重载`Decoder`的`decode`方法添加由`dict`转换为自定义类的逻辑。 

```py
import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def user_hook(dic):
    if dic['name']:
        return User(dic['name'], dic['age'])
    return dic


class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {'name': obj.name, 'age': obj.age}
        return json.JSONEncoder.default(obj)


class UserDecoder(json.JSONDecoder):
    def decode(self, s):
        dic = super().decode(s)
        return User(dic['name'], dic['age'])


# override __init__ method
class UserDecoder2(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self)
        self.object_hook = user_hook


user = User('Jake', 20)

boy_encode_str = json.dumps(user, cls=UserEncoder)

new_user2 = json.loads(boy_encode_str, cls=UserDecoder2)
print(new_user2, type(new_user2))
# {'name': 'Jake', 'age': 20} <class 'dict'>

new_user = json.loads(boy_encode_str, cls=UserDecoder)
print(new_user.name, new_user.age, sep=' -> ')
# Jake -> 20
```



