import functools
import logging
import time


def run_time(function):
    """" 函数运行时间 """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        _start = time.time()
        result = function(*args, **kwargs)
        _end = time.time()
        logging.info(f"name:{function.__name__:<15} time:{_end - _start}")
        return result

    return wrapper
