import sys
import logging

import ___


def test():
    x = 2
    logging.info(sys.getsizeof(x))
    logging.info(sys.getsizeof(sys.getsizeof))
    logging.info(sys.getsizeof('this'))
    logging.info(sys.getsizeof('this also'))


if __name__ == '__main__':
    test()
