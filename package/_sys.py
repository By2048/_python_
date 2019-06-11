import sys
import logging

import base

x = 2
logging.info(sys.getsizeof(x))
logging.info(sys.getsizeof(sys.getsizeof))
logging.info(sys.getsizeof('this'))
logging.info(sys.getsizeof('this also'))
