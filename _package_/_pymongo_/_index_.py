from _._server_ import mongo_client

from pymongo.collection import Collection
from pymongo.helpers import _gen_index_name


def check_collection_index(database: str, collection: str,
                           keys: list = None, name: str = None, background=True, unique=True):
    """ 检查数据库索引是否创建,没有则创建相关索引

    :param database: 需要检查的数据库
    :param collection: 需要检查的表
    :param keys: 需要进索引的字段
    :param name: 索引名
    :param background: 参考PyMongo相关文档
    :param unique: 参考PyMongo相关文档
    """

    db_collection: Collection = mongo_client[database][collection]
    result = db_collection.index_information()

    if keys:
        _name_ = _gen_index_name(keys)
        if not name:
            name = _name_

    if name not in result:
        db_collection.create_index(keys, name=name, background=background, unique=unique)
