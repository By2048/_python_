import json
import requests
try:
    from .config import *
except ImportError:
    from config import *


test_link='https://wall.alphacoders.com/api2.0/get.php?auth={}&method=category&id=10&page=10&info_level=2'.format(api_code)

json_data=requests.get(test_link)

print(json_data.json())

