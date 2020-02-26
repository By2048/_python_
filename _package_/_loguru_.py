from loguru import logger

logger.debug("That's it, beautiful and simple logging!")


# https://github.com/Delgan/loguru


@logger.catch(level='INFO')
def my_function(x, y, z):
    return 1 / (x + y + z)


my_function(0, 0, 0)


# logger.opt(record=True).info("Current line is: {record[line]}")
# logger.opt(lazy=True).debug("If sink <= DEBUG: {x}", x=lambda: math.factorial(2 ** 5))


# logger.add("output.log", backtrace=True, diagnose=True)  # Set 'False' to not leak sensitive data in prod


def func(a, b):
    return a / b


def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("What?!")


nested(0)
