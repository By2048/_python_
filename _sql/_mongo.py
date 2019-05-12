import logging
from datetime import datetime
from pprint import pprint, pformat

from pymongo import MongoClient
from pymongo import ReturnDocument

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)1.1s %(asctime)s.%(msecs)d %(module)9s:%(lineno)3d] %(message)s',
    datefmt='%H:%M:%S'
)

HOST = '192.168.0.99'
PORT = 27017
USER = 'root'
PWD = "123456"

MONGODB = f"mongodb://{USER}:{PWD}@{HOST}:{PORT}"
logging.info(f'MONGODB : {MONGODB}')
client = MongoClient(MONGODB)


def other():
    # 显示所有表
    logging.info(client.test.list_collection_names())


def find():
    for item in client.test.device.find({}):
        logging.info(item)


class CRUD(object):
    def insert(self):
        data = {'name': 111}
        logging.info(data)
        client.demo.test.insert_one(data)

        data = {'name': 222}
        logging.info(data)
        client.demo.test.insert_many([data])

    def delete(self):
        result = client.demo.test.delete_one({'name': 111})
        logging.info(result.deleted_count)
        logging.info(result.raw_result)

        result = client.demo.test.delete_many({})
        logging.info(result.deleted_count)
        logging.info(result.raw_result)

    def auto_increase_id(self):
        # client.demo.test.insert_one({'name': 'max_id', 'value': 1})
        result = client.demo.test.find_one_and_update(
            {"name": "max_id"},
            {"$inc": {"value": 1}},
            return_document=ReturnDocument.BEFORE
        )

        logging.info(result)

        # find_one_and_delete()
        # find_one_and_replace()
        # find_one_and_update()


class Other(object):

    def index(self):
        index_info = client.demo.test.index_information()
        logging.info(index_info)

        # index_info = client.demo.test.create_index([('name', 1)], background=True, name='name_index')
        # logging.info(index_info)

        # client.demo.test.drop_index('name_index')

    def collection(self):
        names = client.demo.list_collection_names()
        breakpoint()
        logging.info(names)


def test():
    pass


if __name__ == '__main__':
    test()

    # CRUD().insert()
    # CRUD().delete()
    # CRUD().auto_increase_id()

    # Other().index()
    Other().collection()
