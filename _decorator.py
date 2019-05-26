import logging

import base


def decorator_a(func):
    logging.info('start a')

    def inner_a(*args, **kwargs):
        logging.info('run a')
        return func(*args, **kwargs)

    return inner_a


def decorator_b(func):
    logging.info('start b')

    def inner_b(*args, **kwargs):
        logging.info('run b')
        return func(*args, **kwargs)

    return inner_b


@decorator_b
@decorator_a
def f(x):
    logging.info('start f')
    return x * 2


f(1)
