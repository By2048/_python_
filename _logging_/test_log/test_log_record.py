import os
import copy
import functools
import logging
import logging.config
import logging.handlers

logger = logging.getLogger()


class Log(object):
    handler = None

    def acquire(self, name):
        _logger = logging.getLogger('__log__')
        _handler = logging.handlers.TimedRotatingFileHandler(filename=name, when="D", interval=1, backupCount=7)
        _formatter = logging.Formatter('[%(asctime)s.%(msecs)3d %(module)15s:%(lineno)3d] %(message)s')
        _handler.setFormatter(_formatter)
        _logger.setLevel(logging.INFO)
        _logger.addHandler(_handler)
        _logger.propagate = False
        self.handler = _handler
        return _logger

    def release(self):
        pass


log = Log().acquire('test')
Log.release()

#
# def log(logger, name):
#     def decorator(function):
#         @functools.wraps(function)
#         def inner(self=None, *args, **kwargs):
#             _path = os.path.dirname(os.path.abspath(__file__))
#
#             _file = getattr(self, name)
#             filename = os.path.join(_path, f'{_file}.log')
#
#             global logger
#             logger_backup = copy.deepcopy(logger)
#             logger = _logger
#             result = function(self, *args, **kwargs)
#             _logger.removeHandler(_handler)
#             logger = logger_backup
#
#             return result
#
#         return inner
#
#     return decorator

#
# class C(object):
#     def __init__(self):
#         self.id = '_id_'
#         self.name = '_name_'
#
#     @log('id')
#     def a(self):
#         logger.info('a')
#         logger.info('a')
#         logger.info('a')
#
#     @log('name')
#     def b(self):
#         logger.info('b')
#         logger.info('b')
#         logger.info('b')
#
#
# @log('_c_')
# def c(qwe, asd):
#     logger.info(f'c {qwe} {asd}')
#
#
# if __name__ == '__main__':
#     # C().a()
#     # C().b()
#     c(123, asd='asdsdfgasg')
