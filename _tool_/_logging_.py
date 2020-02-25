import logging


def init_logging_mini():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(message)s',
        datefmt='%H:%M:%S'
    )


def init_logging_base():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(funcName)11s:%(lineno)3d | %(message)s',
        datefmt='%H:%M:%S'
    )


def init_logging_detail():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s %(asctime)s.%(msecs)3d %(module)s/%(funcName)s:%(lineno)d] %(message)s',
        datefmt='%H:%M:%S'
    )
