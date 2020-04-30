import json
from pprint import pprint

from pymongo import MongoClient

db = MongoClient("mongodb://{user}:{password}@{host}:{port}")
mongo = db['{collection_name}']
result = []
collections = mongo.list_collection_names()
for i in collections:
    result.append({"db_name": i, "size": mongo.command("collstats", i)["size"] / 1024 / 1024})

result = sorted(result, key=lambda x: x['size'], reverse=True)

pprint(result)




def get_size():
    db = mongo_client.ebdb_smartsys

    data = db.command("collstats", "ebc_devices_cookbook")
    pprint(data)

