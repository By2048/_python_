import time
from datetime import datetime
import logging
import json

import requests

data = requests.get('http://www.baidu.com').text
logging.info(data)


