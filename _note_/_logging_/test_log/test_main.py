import logging

try:
    from test.test_log.test_log_record import log
except ImportError:
    from .test_log_record import log

logger = logging.getLogger()


class C(object):
    def __init__(self):
        self.id = '_id_'
        self.name = '_name_'

    @log(logger, 'id')
    def a(self):
        logger.info('a')
        logger.info('a')
        logger.info('a')

    # @log('name')
    # def b(self):
    #     logger.info('b')
    #     logger.info('b')
    #     logger.info('b')


if __name__ == '__main__':
    C().a()
    # C().b()
