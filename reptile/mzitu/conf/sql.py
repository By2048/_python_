import pymongo

MONGO_HOST = '192.168.0.99'
MONGO_PORT = 27017
MONGO_DATABASE = 'reptile'
MONGO_USER = 'admin'
MONGO_PASSWORD = '123456789'

client = pymongo.MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}")
db_reptile = client[MONGO_DATABASE]
