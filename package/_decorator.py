import functools
import time


# def print_run_time(func):
#     def wrapper(*args, **kw):
#         local_time = time.time()
#         func(*args, **kw)
#         print
#         'current Function [%s] run time is %.2f' % (func.__name__, time.time() - local_time)
#
#     return wrapper
from typing import Any


def log_time(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        time_start = time.time()
        function(*args, **kwargs)
        time_end = time.time()
        print("--> name:{:<15} time:{}".format(function.__name__, time_end - time_start))

    return wrapper


@log_time
def a():
    if True:
        print(123)
        print(456)


class B():
    @log_time
    def bb(self):
        print('qwe')

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o)

    def __setattr__(self, name: str, value: Any) -> None:
        super().__setattr__(name, value)


if __name__ == '__main__':
    a()

    b = B()
    b.bb()
