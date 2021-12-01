import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)1.1s %(asctime)s.%(msecs)3d %(module)9s:%(lineno)3d] %(message)s',
    datefmt='%H:%M:%S'
)

logging.info("log")
