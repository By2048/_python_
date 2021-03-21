import json
import time
import logging
import functools
import inspect
from json import JSONDecodeError
from pprint import pprint

import redis
from flask import jsonify, request

try:
    from _tool_ import _logging_
except ImportError:
    from . import _logging_

_logging_.init_logging_mini()


def run_time(function):
    """ function run time """

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        logging.info(f"F:{function.__name__} -> T:{end - start}")
        return result

    return wrapper


def cache(key: str = "", ex: int = 60):
    def decorator(function):
        @functools.wraps(function)
        def inner(*args, **kwargs):
            db = redis.Redis(connection_pool=redis_conn_pool)
            data = db.get(key)

            if data:
                try:
                    data = json.loads(data)
                except JSONDecodeError as e:
                    logging.exception(e)

            if data:
                return data

            result = function(*args, **kwargs)
            value = json.dumps(result, ensure_ascii=False)
            db.set(key, value, ex)

            return result

        return inner

    return decorator


def cache_request(ex: int = 60):
    def decorator(function):
        @functools.wraps(function)
        def inner(*args, **kwargs):

            if not request:
                raise Exception('not flask request')

            _url = request.path.strip('/')
            _get = ['='.join(item) for item in request.args]
            _post = ['='.join(item) for item in request.args]
            _get = '&'.join(sorted(_get))
            _post = '&'.join(sorted(_post))
            key = f"{_url}:{_get}:{_post}"

            db = redis.Redis(connection_pool=redis_conn_pool)
            data = db.get(key)

            if data:
                try:
                    data = json.loads(data)
                except JSONDecodeError as e:
                    logging.exception(e)

            if data and isinstance(data, dict):
                return jsonify(data)

            result = function(*args, **kwargs)
            value = result.json
            value = json.dumps(value, ensure_ascii=False)
            db.set(key, value, ex)

            return result

        return inner

    return decorator
