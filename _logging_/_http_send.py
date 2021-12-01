import time
import logging
import logging.handlers

logger = logging.getLogger(__name__)

server = '127.0.0.1:5000'
path = '/'
method = 'GET'

sh = logging.handlers.HTTPHandler(server, path, method=method)

logger.addHandler(sh)
logger.setLevel(logging.DEBUG)

while True:
    time.sleep(3)
    logger.info("Test message.")
