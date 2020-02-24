import logging
import logging.handlers
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s')
logging.getLogger().addHandler(logging.handlers.DatagramHandler('127.0.0.1', 51010))

while True:
    logging.debug("This shouldn't show up")
    logging.info("This should show up")
    time.sleep(3)

