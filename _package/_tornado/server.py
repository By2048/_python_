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


class AsyncRequestHandler(tornado.web.RequestHandler):
    """Base class for request handlers with `asyncio` coroutines support.
    It runs methods on Tornado's ``AsyncIOMainLoop`` instance.
    Subclasses have to implement one of `get_async()`, `post_async()`, etc.
    Asynchronous method should be decorated with `@asyncio.coroutine`.
    Usage example::
        class MyAsyncRequestHandler(AsyncRequestHandler):
            @asyncio.coroutine
            def get_async(self):
                html = yield from self.application.http.get('http://python.org')
                self.write({'html': html})
    You may also just re-define `get()` or `post()` methods and they will be simply run
    synchronously. This may be convinient for draft implementation, i.e. for testing
    new libs or concepts.
    """

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        """Handle GET request asyncronously, delegates to
        ``self.get_async()`` coroutine.
        """
        yield self._run_method('get', *args, **kwargs)

    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        """Handle POST request asyncronously, delegates to
        ``self.post_async()`` coroutine.
        """
        yield self._run_method('post', *args, **kwargs)

    @asyncio.coroutine
    def _run_async(self, coroutine, future_, *args, **kwargs):
        """Perform coroutine and set result to ``Future`` object."""

        try:
            result = yield from coroutine(*args, **kwargs)
            future_.set_result(result)
        except Exception as e:
            future_.set_exception(e)
            print(traceback.format_exc())

    def _run_method(self, method_, *args, **kwargs):
        """Run ``get_async()`` / ``post_async()`` / etc. coroutine
        wrapping result with ``tornado.concurrent.Future`` for
        compatibility with ``gen.coroutine``.
        """
        coroutine = getattr(self, '%s_async' % method_, None)

        if not coroutine:
            raise tornado.web.HTTPError(405)

        future_ = tornado.concurrent.Future()
        asyncio.async(
            self._run_async(coroutine, future_, *args, **kwargs)
        )

        return future_


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        sum = 0
        for i in range(100000):
            sum += i
        self.write("block sum " + str(sum))
        self.finish()
    # ab -n 1000 -c 200 http://192.168.0.97:4556/main


class NoBlockMainHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(4)

    @run_on_executor
    def run(self):
        sum = 0
        for i in range(100000):
            sum += i
        return sum

    @gen.coroutine
    def get(self):
        sum = yield self.run()
        self.write('no block sum ' + str(sum))
        self.finish()
    # ab -n 1000 -c 200 http://192.168.0.97:4556/main_no_block




class NoBlockRedisHandlerA(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(10)

    @run_on_executor(executor='executor')
    def get_sum(self):
        sum = 0
        for i in range(10000000):
            sum += i
        logging.error(sum)

    async def run(self):
        db = self.application.redis
        key = 'test_' + str(1)
        value = await db.get(key)
        return value

    @tornado.gen.coroutine
    def get(self):
        # value = self.run()
        data = yield self.run()
        if data == '1':
            data = '111111'
        else:
            data = '222222'
        self.get_sum()
        self.write(data)
        self.finish()
    # ab -n 1000 -c 200 http://192.168.0.97:4556/redis_a_no_block


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
    # @tornado.gen.coroutine
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





POOL = pools.Pool(dict(host=config.MYSQL_HOST, port=config.MYSQL_PORT, user=config.MYSQL_USER, passwd=config.MYSQL_PWD,
                       db=config.MYSQL_OPEN_DATABASE), max_idle_connections=30, max_recycle_sec=3)


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
        yield tools.set("SELECT * FROM ebt_api")
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
            (r"/main", MainHandler),
            (r"/main_no_block", NoBlockMainHandler),

            (r"/redis", RedisHandler),
            (r"/redis_no_block", NoBlockRedisHandler),

            (r"/redis_a", RedisHandlerA),
            (r"/redis_a_no_block", NoBlockRedisHandlerA),

            (r"/redis_test", RedisTestHandler),
            (r"/redis_test_no_block", NoBlockRedisTestHandler),

            (r"/mongo", MongoDBHandler),
            (r"/mongo_no_block", NoBlockMongoDBHandler),

            (r"/mysql", MySQLHandler),
            (r"/mysql_no_block", NoBlockMySQLHandler),
        ]

        super().__init__(handlers, debug=True)

    def init_with_loop(self, loop):
        self.redis = loop.run_until_complete(
            aioredis.create_redis((config.REDIS_HOST, config.REDIS_PORT), password=config.REDIS_PWD,
                                  db=config.REDIS_DB, loop=loop)
        )


async def redis_get(redis: 'aioredis.create_redis', key):
    value = await redis.get(key)
    # redis.close()
    # await redis.wait_closed()
    logging.info(value)
    return value


async def redis_set(redis: 'aioredis.create_redis', key, value):
    result = await redis.set(key, value)
    redis.close()
    await redis.wait_closed()
    return result


if __name__ == "__main__":
    app = Application()
    app.listen(4556)
    loop = asyncio.get_event_loop()
    app.init_with_loop(loop)

    tornado.ioloop.IOLoop.current().start()
