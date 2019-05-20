from datetime import datetime
import logging

import base

timestramp = 1273969203.1234

date = datetime.fromtimestamp(timestramp)
logging.info([date, type(date)])

date = datetime.utcfromtimestamp(timestramp)
logging.info([date, type(date)])

logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
