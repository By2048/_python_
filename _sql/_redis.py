import json

import redis
import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)1.1s %(asctime)s.%(msecs)3d %(module)9s:%(lineno)3d] %(message)s',
    datefmt='%H:%M:%S'
)

HOST, PORT, PWD, DB, MAX = '192.168.0.99', 6379, "123456", 9, 100
logging.info(f'host:{HOST}    port:{PORT}    pwd:{PWD}    db:{DB}')

pool = redis.ConnectionPool(max_connections=MAX, host=HOST, port=PORT, db=DB, password=PWD)
db = redis.Redis(connection_pool=pool, decode_responses=True)


# db = redis.Redis(host=HOST, port=PORT, db=DB, password=PWD, decode_responses=True)


def _set():
    db.set('name', 'qwer1234', ex=None, px=None, nx=False, xx=False)
    db.setex('name', 100, 'qwer1234')


def _get():
    logging.info(db.get('name'))

    logging.info(db.keys('*'))
    for key in db.keys('key:*'):
        logging.info(key.decode() + ' -> ' + db.get(key.decode()).decode())


def _list():
    db.delete('test_list')
    db.rpush('test_list', 1)
    db.rpush('test_list', 2, 3, json.dumps([1, 2, 3]))
    # db.expire('test_list', None)
    logging.info(db.lrange('test_list', 0, -1))


def test():
    pass


if __name__ == '__main__':
    # set()
    # get()
    # test()
    # _list()
    pass
