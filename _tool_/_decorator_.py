import time
import logging
import functools

try:
    from _tool_ import _logging_
except ImportError:
    from . import _logging_

_logging_.init_logging_mini()


def run_time(function):
    """ function run time """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        logging.info(f"F:{function.__name__} -> T:{end - start}")
        return result

    return wrapper


def log(function):
    """ 输出一些特殊变量 """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        for key, value in locals().items():
            if key.startswith(("data", "result")):
                print(f"F:{function.__name__} | K:{key} V:{value}")
        return result

    return wrapper
