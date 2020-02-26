import time
import json
from datetime import datetime

import requests

data = requests.get('http://www.baidu.com').text
data = data.strip()

print(data)
