import logging

import stackprinter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

stackprinter.set_excepthook(style='color')


def fun(x, y, z):
    return 1 / (x + y + z)


try:
    fun(0, 0, 0)
except:
    # grab the current exception, print the traceback to stderr:
    stackprinter.show()

    # ...or only get a string, e.g. for logging:
    # logger.error(stackprinter.format())
