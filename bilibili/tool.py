import hashlib
import os
import time
import re

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

try:
    from .config import *
except:
    from config import *


def get_md5(path):
    if not os.path.isfile(path):
        return
    hash=hashlib.md5()
    file=open(path,'rb')
    while True:
        byte=file.read(8096)
        if not byte:
            break
        hash.update(byte)
    file.close()
    md5=hash.hexdigest()
    md5=md5.lower()
    return md5

def page_down(chrome,cnt):
    for i in range(cnt):
        print('page down ...'+str(i))
        ActionChains(chrome).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(0.5)

# html='''background-size: cover; background-position: center top; background-image: url("http://i0.hdslb.com/bfs/vc/72d8fd43e585a5b0f468a90867b6c3e7656f626e.png@512w_384h_1e.webp");'''
# http://i0.hdslb.com/bfs/vc/72d8fd43e585a5b0f468a90867b6c3e7656f626e.png
def get_down_link(html):
    url_match = re.search("url.*\)", html)
    url_group = url_match.group()
    link_match = re.search(r'(http)(.*)(\.png|\.jpg)', url_group)
    link_group = link_match.group()
    return link_group




















