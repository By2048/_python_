import json
from pprint import pprint

from pymongo import MongoClient

db = MongoClient("mongodb://smartsys:smartsys.com@s71.53iq.com:30000")
mongo = db["ebdb_smartsys"]
result = []
collections = mongo.list_collection_names()
for i in collections:
    result.append({"db_name": i, "size": mongo.command("collstats", i)["size"] / 1024 / 1024})

result = sorted(result, key=lambda x: x['size'], reverse=True)

pprint(result)
