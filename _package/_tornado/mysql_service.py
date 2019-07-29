# coding=utf-8
import time
import logging
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

from tornado.concurrent import Future

import redis
import pymysql
import tornado.ioloop
import tornado.web
import tornado.options
from tornado import gen
from tornado.concurrent import run_on_executor
from tornado.httpclient import AsyncHTTPClient

import tornado_mysql
import aioredis
import pymongo
import motor.motor_tornado
from tornado_mysql import pools
import tools

import config

tornado.options.parse_command_line()

logging.basicConfig(level=logging.INFO)



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


class MySQLHandler(tornado.web.RequestHandler):
    def get(self):
        db = pymysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USER,
                             passwd=config.MYSQL_PWD, db=config.MYSQL_OPEN_DATABASE, charset='UTF8',
                             cursorclass=pymysql.cursors.DictCursor)
        cur = db.cursor()
        sql = "SELECT * FROM ebt_api"
        cur.execute(sql)
        data = cur.fetchall()
        apis = {}
        for index, item in enumerate(data):
            apis[str(index)] = str(item)
        logging.error(apis)
        cur.close()
        db.close()
        self.write(apis)
        self.finish()
    # ab -n 1000 -c 200 http://192.168.0.97:4556/mysql


class NoBlockMySQLHandler(tornado.web.RequestHandler):
    # @gen.coroutine
    # def get_data(self, command):
    #     logging.info('---')
    #     conn = yield tornado_mysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USER,
    #                                        passwd=config.MYSQL_PWD, db=config.MYSQL_OPEN_DATABASE)
    #     cur = conn.cursor()
    #     yield cur.execute(command)
    #     result = {}
    #     for index, item in enumerate(cur):
    #         result[str(index)] = str(item)
    #     cur.close()
    #     conn.close()
    #     logging.info(result)

    @gen.coroutine
    def get(self):
        yield set("SELECT * FROM ebt_api")
        self.finish('123')

    # @gen.coroutine
    # def get(self):
    #     conn = yield tornado_mysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USER,
    #                                        passwd=config.MYSQL_PWD, db=config.MYSQL_OPEN_DATABASE)
    #     cur = conn.cursor()
    #     yield cur.execute("SELECT * FROM ebt_api where ebf_api_id='1'")
    #     logging.error(cur)
    #     logging.info(type(cur))
    #     apis = {}
    #     logging.info(cur.description)
    #     for index, item in enumerate(cur):
    #         apis[str(index)] = str(item)
    #
    #     if apis == {}:
    #         self.write('None')
    #     else:
    #         self.write(apis)
    #
    #     cur.close()
    #     conn.close()
    #     self.finish()

    # ab -n 1000 -c 200 http://192.168.0.97:4556/mysql_no_block
    """
    @gen.coroutine
    def get(self):
        conn = yield tornado_mysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USER,
                                           passwd=config.MYSQL_PWD, db=config.MYSQL_OPEN_DATABASE)
        cur = conn.cursor()
        yield cur.execute("SELECT * FROM ebt_api")
        apis = {}
        for index, item in enumerate(cur):
            apis[str(index)] = str(item)
        cur.close()
        conn.close()
        self.write(apis)
        self.finish()
    """


class Application(tornado.web.Application):
    def __init__(self):
        # Prepare IOLoop class to run instances on asyncio
        tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')
        handlers = [
            (r"/mysql", MySQLHandler),
            (r"/mysql_no_block", NoBlockMySQLHandler),
        ]

        super().__init__(handlers, debug=True)



if __name__ == "__main__":
    app = Application()
    app.listen(4556)
    loop = asyncio.get_event_loop()
    tornado.ioloop.IOLoop.current().start()
