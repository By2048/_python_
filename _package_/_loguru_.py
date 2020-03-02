import math

from loguru import logger

# https://github.com/Delgan/loguru


logger.info('message')
logger.error('message')
logger.debug('message')
logger.warning('message')
logger.opt(record=True).info("current line is: {record[line]}")
logger.opt(lazy=True).debug("If sink <= DEBUG: {x}", x=lambda: math.factorial(2 ** 5))
# logger.add("output.log", backtrace=True, diagnose=True)

logger.info(f"\n{'=' * 999}")


@logger.catch()
def test(x, y, z):
    return 1 / (x + y + z)


test(0, 0, 0)

logger.info(f"\n{'=' * 999}")


def test_1(a, b):
    return a / b


def test_2(a, b):
    try:
        test_1(a, b)
    except Exception as e:
        logger.exception(f"What? {e}")


test_2(1, 0)
