import os
import urllib
import urllib.request
import time
import math
import sys
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver as webdriver
# import selenium.webdriver.support.ui as ui
# from selenium.webdriver.common.keys import Keys


chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

links=[
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com",
"http://www.baidu.com"
]


chrome = webdriver.Chrome(chrome_path)
# geckodriver
# chrome = webdriver.Firefox()
# chrome.get("http://www.baidu.com")

for link in links:
    print(link)

def run_js(chrome,jss):
    for js in jss:
        print(js)
        chrome.execute_script(js)
    print('run over -----')
    time.sleep(1)

def refresh_handles():
    return chrome.window_handles

setp = 3
for i in range(0,len(links),setp):

    jss = []
    for link in links[i:i + setp]:

        js = "window.open(\"{0}\")".format(link)
        jss.append(js)
    run_js(chrome,jss)

    handles= chrome.window_handles

    print('1 --- ',end='')
    print("\n".join(handles))

    for handle in handles[1:]:
        chrome.switch_to.window(handle)
        time.sleep(1)
        chrome.close()
        # handles=chrome.window_handles

    chrome.switch_to_window(handles[0])
    handles=chrome.window_handles

    # WebDriverWait(chrome, 10).until(lambda d: len(d.window_handles) == 1)
    print('2 --- ',end='')
    print("\n".join(handles))


    time.sleep(5)