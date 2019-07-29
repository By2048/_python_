import os
import time
import logging
import logging.handlers

# log_message_format = "[%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)d] %(message)s"
log_path = os.path.join(os.getcwd(), 'log')
log_message_format = '[%(levelname)1.1s %(asctime)s.%(msecs)3d %(module)15s:%(lineno)3d] %(message)s'
log_time_format = "%Y-%m-%d %H:%M:%S"

"""
%(levelno)s	    打印日志级别的数值
%(levelname)s	打印日志级别名称
%(pathname)s	打印当前执行程序的路径
%(filename)s	打印当前执行程序名称
%(funcName)s	打印日志的当前函数
%(lineno)d	    打印日志的当前行号
%(asctime)s	    打印日志的时间
%(thread)d	    打印线程id
%(threadName)s	打印线程名称
%(process)d	    打印进程ID
%(message)s	    打印日志信息
"""


def test_function():
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warn message')
    logging.error('error message')
    logging.critical('critical message')
    time.sleep(3)
    try:
        a = 1 / 0
        logging.info(a)
    except Exception as e:
        logging.exception(e)


def test_file_handler():
    handler = logging.FileHandler(filename=log_path)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(log_message_format, log_time_format))
    logging.getLogger().addHandler(handler)
    test_function()
    logging.getLogger().removeHandler(handler)


def test_rotating_file_handler():
    handler = logging.handlers.RotatingFileHandler(filename=log_path, maxBytes=300, backupCount=3)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(log_message_format, log_time_format))
    logging.getLogger().addHandler(handler)
    test_function()
    logging.getLogger().removeHandler(handler)


def test_timed_rotating_file_handler():
    handler = logging.handlers.TimedRotatingFileHandler(filename=log_path, when='S', interval=3, backupCount=3)
    handler.suffix = '%Y.%m.%d %H.%M.%S'
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(log_message_format, log_time_format))
    logging.getLogger().addHandler(handler)
    test_function()
    logging.getLogger().removeHandler(handler)


if __name__ == '__main__':
    test_file_handler()
    # test_rotating_file_handler()
    # test_timed_rotating_file_handler()
