import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s %(module)s/%(funcName)s/%(lineno)d %(asctime)s.%(msecs)3d] %(message)s',
    datefmt='%H:%M:%S'
)

logging.info('init logging config\n')
