import functools
import logging
import time

import _conf


def run_time(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        _start = time.time()
        result = function(*args, **kwargs)
        _end = time.time()
        logging.info(f"{function.__name__:<15} {_end - _start}")
        return result

    return wrapper
