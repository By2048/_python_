import random

import _conf_
from _tool_._decorator_ import run_time

MAX_LEN = 1_000_000
MAX_RANDOM = 1_000_000
MAX_SEARCH = 10_000

_list_ = []
_set_ = set()
_dict_ = dict()


def init():
    for i in range(0, MAX_LEN):
        item = random.randint(0, MAX_RANDOM)
        _list_.append(item)
        _set_.add(item)
        _dict_[i] = item


@run_time
def test_set():
    for i in range(MAX_SEARCH):
        _ = i in _set_


@run_time
def test_dict():
    for i in range(MAX_SEARCH):
        _ = i in _dict_


@run_time
def test_list():
    for i in range(MAX_SEARCH):
        _ = i in _list_


if __name__ == '__main__':
    init()
    test_set()
    test_dict()
    test_list()
