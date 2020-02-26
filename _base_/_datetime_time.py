import logging
from datetime import datetime

data = 1273969203.1234

date = datetime.fromtimestamp(data)
logging.info([date, type(date)])

date = datetime.utcfromtimestamp(data)
logging.info([date, type(date)])

logging.info(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
