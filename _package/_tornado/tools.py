# coding=utf-8
import logging
import tornado_mysql
import config
from tornado import gen


@gen.coroutine
def get(command):
    conn = yield tornado_mysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USER,
                                       passwd=config.MYSQL_PWD, db=config.MYSQL_OPEN_DATABASE)
    cur = conn.cursor()
    yield cur.execute(command)
    result = {}
    for index, item in enumerate(cur):
        result[str(index)] = str(item)
    cur.close()
    conn.close()
    return result


@gen.coroutine
def set(command):
    logging.error('qwer1123234')

    conn = yield tornado_mysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USER,
                                       passwd=config.MYSQL_PWD, db=config.MYSQL_OPEN_DATABASE)
    cur = conn.cursor()
    yield cur.execute(command)
    logging.error('qwer1234')



