import random

import _conf_
from _tool_._decorator_ import run_time

MAX_LEN = 100_000
MAX_RANDOM = 100_000
MAX_SEARCH = 3_000

_list = []
_set = set()
_dict = dict()


@run_time
def init():
    for i in range(0, MAX_LEN):
        item = random.randint(0, MAX_RANDOM)
        _list.append(item)
        _set.add(item)
        _dict[i] = item


@run_time
def test_set():
    for i in range(MAX_SEARCH):
        _ = i in _set


@run_time
def test_dict():
    for i in range(MAX_SEARCH):
        _ = i in _dict


@run_time
def test_list():
    for i in range(MAX_SEARCH):
        _ = i in _list


if __name__ == '__main__':
    init()
    test_set()
    test_dict()
    test_list()
