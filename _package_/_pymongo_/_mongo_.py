import logging

from pymongo import ReturnDocument

from _._server_ import mongo_client as client


class CRUD(object):
    @staticmethod
    def insert():
        data = {'name': 111}
        logging.info(data)
        result = client.demo.test.insert_one(data)
        print(result)

        data = {'name': 222}
        logging.info(data)
        client.demo.test.insert_many([data])

    @staticmethod
    def delete():
        result = client.demo.test.delete_one({'name': 111})
        logging.info(result.deleted_count)
        logging.info(result.raw_result)

        result = client.demo.test.delete_many({})
        logging.info(result.deleted_count)
        logging.info(result.raw_result)

    @staticmethod
    def auto_increase_id():
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

    @staticmethod
    def updata():
        # mongo.ebdb_smartsys.ebc_devices_cookbook.update(
        #     {'_id': ObjectId(_id)},
        #     {
        #         '$set': {
        #             'standard_parameter': parameter,
        #             'standard_parameter_device_name': rule['name']
        #         },
        #         '$unset': {'device_name': ''}
        #     }
        # )
        pass


class Other(object):
    @staticmethod
    def index():
        index_info = client.demo.test.index_information()
        logging.info(index_info)

        # index_info = client.demo.test.create_index([('name', 1)], background=True, name='name_index')
        # logging.info(index_info)

        # client.demo.test.drop_index('name_index')

    @staticmethod
    def collection():
        names = client.demo.list_collection_names()
        breakpoint()
        logging.info(names)

    @staticmethod
    def all_collection():
        # 显示所有表
        logging.info(client.test.list_collection_names())

    @staticmethod
    def find_all():
        for item in client.test.device.find({}):
            logging.info(item)


if __name__ == '__main__':
    CRUD.insert()
    CRUD.delete()
    CRUD.updata()
    CRUD.auto_increase_id()

    Other.index()
    Other.collection()
