from collections import \
    deque, defaultdict, namedtuple, Counter, OrderedDict, ChainMap, \
    UserDict, UserList, UserString

import pysnooper


# https://docs.python.org/zh-cn/3/library/collections.html
# https://docs.python.org/zh-cn/3.7/library/collections.html

def _namedtuple_():
    # namedtuple 创建具有命名字段的tuple子类的工厂函数
    Card = namedtuple('Card', ['rank', 'suit'])
    c1 = Card('A', '红桃')
    c2 = Card('K', '黑桃')
    print(c1.rank, c1.suit)
    print(c2.rank, c2.suit)


@pysnooper.snoop()
def _deque_():
    item = deque()
    item.append("b")  # 在尾部插入数据
    item.appendleft("a")  # 在头部插入数据
    item.append('d')
    item.insert(2, "c")
    xxx = item.count('a')
    item.clear()


def _defaultdict_():
    item = defaultdict(set)
    item['key'].add(1)
    item['key'].add(2)
    item['key'].add(3)
    print(item)
    print(item['key'])
    print(item['-key-'])

    item = defaultdict(list)
    item['key'].append(1)
    item['key'].append(2)
    item['key'].append(3)
    print(item)
    print(item['key'])
    print(item['-key-'])

    item = defaultdict(dict)
    item['key'] = 123
    print(item)
    print(item['key'])
    print(item['-key-'])

    item = defaultdict(lambda: '-None-')
    item['key'] = 123
    print(item)
    print(item['key'])
    print(item['-key-'])


def _OrderedDict_():
    xxx = OrderedDict([("name", "-name-"), ("age", '-age-'), ("sex", "-sex-")])
    xxx.setdefault("high-2", '-high-2-')
    xxx["high-1"] = '-high-1-'
    print(xxx.items())
    xxx.move_to_end('name')
    print(xxx.items())


def _Counter_():
    """ 示例 参考源码文档 """
    item = Counter()


def _ChainMap_():
    # 合并多个字典
    dict1 = {'name': 'jim1', 'age': 21}
    dict2 = {'name': 'jim2', 'high': 175}
    dict3 = ChainMap(dict1, dict2)
    print(dict3)
    print(dict3.maps)
    print(dict3['name'])
    dict4 = dict3.new_child({"name": 'jim3'})
    print(dict4)
    print(dict4.parents)
    print(dict4.parents.parents)


if __name__ == '__main__':
    pass
    # _namedtuple_()
    # _deque_()
    # _defaultdict_()
    # _OrderedDict_()
    # _Counter_()
    # _ChainMap_()
