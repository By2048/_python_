# coding=utf-8
import time
import logging
import asyncio
from concurrent.futures.thread import ThreadPoolExecutor

import tornado.ioloop
import tornado.web
import tornado.options
from tornado import gen
from tornado.concurrent import Future
from tornado.concurrent import run_on_executor
from tornado.httpclient import AsyncHTTPClient
import redis
import aioredis

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


class RedisHandler(tornado.web.RequestHandler):
    def get(self):
        connection = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT,
                                 password=config.REDIS_PWD, db=config.REDIS_DB)
        value = connection.get('test_1')
        self.finish(value)
    # ab -n 1000 -c 200 http://192.168.0.97:4556/redis

class NoBlockRedisHandler(AsyncRequestHandler):
    async def get_value(self, key):
        redis = self.application.redis
        value = await redis.get(key)
        return value

    @tornado.gen.coroutine
    def get(self):
        result = yield self.get_value('test_1')
        self.finish(result)
    # ab -n 1000 -c 200 http://192.168.0.97:4556/redis_no_block

class RedisHandlerA(tornado.web.RequestHandler):
    def get_sum(self):
        sum = 0
        for i in range(10000000):
            sum += i
        logging.error(sum)

    def get(self):

        db = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT,
                         password=config.REDIS_PWD, db=config.REDIS_DB)
        key = 'test_' + str(1)
        data = db.get(key)
        if data == '1':
            data = '111111'
        else:
            data = '222222'
        self.get_sum()
        self.write(data)
        self.finish()
    # ab -n 1000 -c 200 http://192.168.0.97:4556/redis_a


class NoBlockRedisHandlerA(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(10)

    @run_on_executor(executor='executor')
    def get_sum(self):
        sum = 0
        for i in range(10000000):
            sum += i
        logging.error(sum)

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


class RedisTestHandler(tornado.web.RequestHandler):
    def get(self):
        connection = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT,
                                 password=config.REDIS_PWD, db=config.REDIS_DB)
        value = connection.get('test_1')
        self.finish(value)
    # ab -n 1000 -c 200 http://192.168.0.97:4556/redis_test


class NoBlockRedisTestHandler(tornado.web.RequestHandler):
    async def get_value(self, key):
        redis = self.application.redis
        value = await redis.get(key)
        return value

    @tornado.gen.coroutine
    def get(self):
        result = yield self.get_value('test_1')
        self.finish(result)
    # ab -n 1000 -c 200 http://192.168.0.97:4556/redis_test_no_block


class Application(tornado.web.Application):
    def __init__(self):
        # Prepare IOLoop class to run instances on asyncio
        tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')
        handlers = [

            (r"/redis", RedisHandler),
            (r"/redis_no_block", NoBlockRedisHandler),

            (r"/redis_a", RedisHandlerA),
            (r"/redis_a_no_block", NoBlockRedisHandlerA),

            (r"/redis_test", RedisTestHandler),
            (r"/redis_test_no_block", NoBlockRedisTestHandler),
        ]

        super().__init__(handlers, debug=True)

    def init_with_loop(self, loop):
        self.redis = loop.run_until_complete(
            aioredis.create_redis((config.REDIS_HOST, config.REDIS_PORT), password=config.REDIS_PWD,
                                  db=config.REDIS_DB, loop=loop)
        )


if __name__ == "__main__":
    app = Application()
    app.listen(4556)
    loop = asyncio.get_event_loop()
    app.init_with_loop(loop)
    tornado.ioloop.IOLoop.current().start()
