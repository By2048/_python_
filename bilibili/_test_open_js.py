import os
import urllib
import urllib.request
import time
import math
import sys
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    from config import *
    from download import *
    from sql import *
    from tool import *
    from image import *
except ImportError:
    from .config import *
    from .download import *
    from .sql import *
    from .tool import *
    from .image import *

links=[
"http://h.bilibili.com/749728",
"http://h.bilibili.com/752736",
"http://h.bilibili.com/740834",
"http://h.bilibili.com/765719",
"http://h.bilibili.com/755273",
"http://h.bilibili.com/13248",
"http://h.bilibili.com/758520",
"http://h.bilibili.com/761004",
"http://h.bilibili.com/666859",
"http://h.bilibili.com/761224",
"http://h.bilibili.com/747787",
"http://h.bilibili.com/760043",
"http://h.bilibili.com/706161",
"http://h.bilibili.com/546947",
"http://h.bilibili.com/683404",
"http://h.bilibili.com/687107",
"http://h.bilibili.com/768633",
"http://h.bilibili.com/748118",
"http://h.bilibili.com/765654",
"http://h.bilibili.com/691685"
]


chrome = webdriver.Chrome(chrome_path)
chrome.get("http://www.baidu.com")

for link in links:
    print(link)

def run_js(chrome,jss):
    for js in jss:
        print(js)
        chrome.execute_script(js,"")
    print('run over -----')

def refresh_handles():
    return chrome.window_handles

setp = 3
for i in range(0,len(links),setp):

    print(chrome.current_url)

    jss = []
    for link in links[i:i + setp]:

        js = "window.open(\"{0}\")".format(link)
        jss.append(js)
    run_js(chrome,jss)

    handles = chrome.window_handles

    print('1 --- ',end='')
    print(handles)

    for handle in handles[1:]:
        chrome.switch_to.window(handle)
        # ActionChains(chrome).send_keys(Keys.CONTROL+'t').perform()
        chrome.close()

    handles=chrome.window_handles

    WebDriverWait(chrome, 10).until(lambda d: len(d.window_handles) == 1)
    print('2 --- ',end='')
    print(handles)

    time.sleep(3)