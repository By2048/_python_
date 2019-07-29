import pickle
import logging
import socket

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 51010))

while True:
    d, _ = s.recvfrom(65536)
    log = pickle.loads(d[4:])
    logger.handle(logging.makeLogRecord(log))
