import functools
import logging
import time

from _tool_ import _logging_

_logging_.init_mini()


def run_time(function):
    """ function run time """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        logging.info(f"𝙁:{function.__name__} -> 𝙏:{end - start}")
        return result

    return wrapper
