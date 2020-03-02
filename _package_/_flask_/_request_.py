from loguru import logger
from flask import Flask, request, Response, g, abort

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    logger.info('before_first_request')


@app.before_request
def before_request():
    logger.info('before_request')


@app.after_request
def after_request(response: Response):
    logger.info('after_request')
    logger.info(response)
    return response


@app.teardown_request
def teardown_request(error):
    logger.info('teardown_request')
    logger.error(error)


@app.errorhandler(500)
def error_handler(error):
    logger.info(f'error_handler {error}')
    return 'ERROR PAGE'


# before_first_request
# before_request
# errorhandler
# after_request
# teardown_request


@app.route('/test_1')
def test_1():
    return 'test_1'


@app.route('/test_2')
def test_2():
    abort(500)


@app.route('/test_3')
def test_3():
    response = Response('message - abort')
    abort(response)


@app.route('/test_4')
def test_4():
    data = None
    try:
        data = 1 / 0
    except Exception as e:
        logger.catch()
    return data


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
