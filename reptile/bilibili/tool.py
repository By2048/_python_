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
    from conf import *
except:
    from .config import *


def get_sha1(path):
    if not os.path.isfile(path):
        return
    hash=hashlib.sha1()
    file=open(path,'rb')
    while True:
        byte=file.read(8096)
        if not byte:
            break
        hash.update(byte)
    file.close()
    sha1=hash.hexdigest()
    sha1=sha1.lower()
    return sha1

def page_down(chrome,cnt):
    for i in range(cnt):
        print('page down ...'+str(i))
        ActionChains(chrome).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(0.5)

# html='''background-size: cover; background-position: center top; background-image-test: url("http://i0.hdslb.com/bfs/vc/72d8fd43e585a5b0f468a90867b6c3e7656f626e.png@512w_384h_1e.webp");'''
# http://i0.hdslb.com/bfs/vc/72d8fd43e585a5b0f468a90867b6c3e7656f626e.png
def get_down_link(html):
    url_match = re.search("url.*\)", html)
    url_group = url_match.group()
    link_match = re.search(r'(http)(.*)(\.png|\.jpg)', url_group)
    link_group = link_match.group()
    return link_group


def list_to_string(list):
    return separator.join(list)

def string_to_list(string):
    list=string.split(separator)
    if len(list)==1 and list[0]=='':
        list=[]
    return list



# ======== Test ========
# sha1=get_sha1('e:\\desktop\\1.jpg')
# print(sha1)









