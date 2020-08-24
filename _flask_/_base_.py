import time
import logging

from flask import Flask, request, Response

logger = logging.getLogger('api')

app = Flask('api')


def before_request():
    request.start_time = time.time()


def after_request(response: Response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['X-Requested-With'] = 'XMLHttpRequest'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with, content-type'
    if not hasattr(request, 'start_time'):
        request.start_time = time.time()
    request.end_time = time.time()
    _time = "{:.3f}".format(request.end_time - request.start_time)
    logger.info(f"ip:{request.remote_addr} code:{response.status_code} time:{_time} path:{request.path}")
    return response


app.before_request(before_request)
app.after_request(after_request)
