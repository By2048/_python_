from random import shuffle
from functools import cmp_to_key

from _tool_._decorator_ import log_test
from _tool_._other_ import run_all_test


def key(item):
    return len(item)


def cmp(a, b):
    return len(a) - len(b)


data = ["1", "1, 2, 3", "1, 2", "1, 2, 3, 4"]


@log_test
def test_1():
    global data
    shuffle(data)
    data = sorted(data, key=cmp_to_key(cmp))
    return data


@log_test
def test_2():
    global data
    shuffle(data)
    data.sort(key=cmp_to_key(cmp))
    return data


@log_test
def test_3():
    global data
    shuffle(data)
    data = sorted(data, key=key)
    return data


@log_test
def test_4():
    global data
    shuffle(data)
    data.sort(key=key)
    return data


if __name__ == '__main__':
    run_all_test(globals())
