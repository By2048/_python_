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


class MongoDBHandler(tornado.web.RequestHandler):
    # def get(self):
    #     db = pymongo.MongoClient(config.MONGODB_CONN)[config.MONGODB_DATABASE]
    #     data = {}
    #     for i in range(30):
    #         key = 'test_' + str(i)
    #         # value = str(i)
    #         # db.tmp.insert_one({"key": key, "value": value})
    #         value = db.tmp.find_one({"key": key})
    #         data[str(i)] = [value['key'], value['value']]
    #     self.write(data)
    #     self.finish()
    def get(self):
        db = pymongo.MongoClient(config.MONGODB_CONN)[config.MONGODB_DATABASE]
        data = {}
        key = 'test_' + str(1)
        value = db.tmp.find_one({"key": key})
        del value['_id']
        self.write(value)
        self.finish()
    # ab -n 1000 -c 200 http://192.168.0.97:4556/mongo


class NoBlockMongoDBHandler(tornado.web.RequestHandler):

    async def find_one(self, key):
        db = motor.motor_tornado.MotorClient(config.MONGODB_CONN)[config.MONGODB_DATABASE]
        value = await db.tmp.find_one({"key": key})
        return value

    @tornado.gen.coroutine
    def get(self):
        key = 'test_' + str(1)
        data = self.find_one(key)
        result = yield data
        del result['_id']
        self.write(result)
        self.finish()

    # ab -n 1000 -c 200 http://192.168.0.97:4556/mongo_no_block


class Application(tornado.web.Application):
    def __init__(self):
        # Prepare IOLoop class to run instances on asyncio
        tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')
        handlers = [
            (r"/mongo", MongoDBHandler),
            (r"/mongo_no_block", NoBlockMongoDBHandler),
        ]

        super().__init__(handlers, debug=True)


if __name__ == "__main__":
    app = Application()
    app.listen(4556)
    loop = asyncio.get_event_loop()
    tornado.ioloop.IOLoop.current().start()
