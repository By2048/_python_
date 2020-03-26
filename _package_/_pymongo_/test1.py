from pprint import pprint
import logging

from bson import ObjectId
from pymongo import MongoClient

from conf.sql import MONGO_71

mongo = MongoClient(MONGO_71)


def update_cookbook_card():
    data = mongo.ebdb_smartsys.ebc_cookbook_card.find({})
    for item in data:
        _id = str(item['_id'])[::-6]
        print(_id, int(_id, 16))
        result = mongo.ebdb_smartsys.ebc_cookbook_card.update(
            {'_id': item['_id']},
            {'$set': {'id': int(_id, 16)}}
        )
        print(result)


def update_cookbook_card_device():
    data = mongo.ebdb_smartsys.ebc_cookbook_card_device.find({})

    for item in data:
        _id = str(str(item['_id'])[::-6])
        _cookbook_card_id = str(item['cookbook_card_id'][::-6])

        result = mongo.ebdb_smartsys.ebc_cookbook_card_device.update(
            {'_id': item['_id']},
            {
                '$set': {
                    'id': int(_id, 16),
                    'cookbook_card_id': int(_cookbook_card_id, 16)
                }
            }
        )
        print(result)


def get_cookbook_card_title():
    data = mongo.ebdb_smartsys.ebc_cookbook_card.find({})
    for item in data:
        _title = item.get('data').get("cook_title")
        if _title:
            print(_title)


def get_size():
    db = mongo.ebdb_smartsys

    data = db.command("collstats", "ebc_devices_cookbook")
    pprint(data)


get_size()

# update_cookbook_card()
# update_cookbook_card_device()
# get_cookbook_card_title()
