import json
import copy
import doctest
import hashlib
import logging
from bson import ObjectId
from datetime import datetime
from enum import Enum



def make_password(data: str):
    md5 = hashlib.md5()
    md5.update(data.encode())
    result = md5.hexdigest()
    return result


if __name__ == '__main__':
    doctest.testmod()
