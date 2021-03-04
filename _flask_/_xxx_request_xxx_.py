import time

from loguru import logger
from flask import Flask, request, Response

app = Flask(__name__)

PORT = 1234


@app.before_first_request
def before_first_request():
    logger.info('before_first_request')


@app.before_request
def before_request():
    logger.info('before_request')
    request.start_time = time.time()


@app.after_request
def after_request(response: Response):
    logger.info('after_request')
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['X-Requested-With'] = 'XMLHttpRequest'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with, content-type'
    if not hasattr(request, 'start_time'):
        request.start_time = time.time()
    request.end_time = time.time()
    _time = "{:.3f}".format(request.end_time - request.start_time)
    print(f"ip:{request.remote_addr} code:{response.status_code} time:{_time} path:{request.path}")
    return response


@app.teardown_request
def teardown_request(error):
    logger.info('teardown_request')
    logger.error(error)


@app.errorhandler(500)
def error_handler(error):
    logger.info(f'error_handler {error}')
    return 'ERROR PAGE'


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    print(f'server start at {PORT}')
    app.run(host='0.0.0.0', port=PORT, debug=True)
