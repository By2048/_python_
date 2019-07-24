import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s %(asctime)s.%(msecs)3d %(module)s/%(funcName)s:%(lineno)d] %(message)s',
    datefmt='%H:%M:%S'
)

logging.info('init logging config\n')
