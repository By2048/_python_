import os
import urllib
import urllib.request
import time
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    from config import *
    from download import *
    from sql import *
except ImportError:
    from .config import *
    from .download import *
    from .sql import *



down_links=[]

chrome=None


# 获取的链接进行转换
def get_down_link(style):
    css='background-size: cover; background-image: url'
    url=style.replace(css,'')[2:-3].split('@')[0]
    return url


# PageDown 模块
def page_down():
    for i in range(40):
        print('page down ...')
        ActionChains = webdriver.common.action_chains.ActionChains
        ActionChains(chrome).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(0.5)

# 获取页面下的所有图片下载链接
def get_all_image_link():
    all_elem=chrome.find_elements_by_class_name('a-fade-in')
    for elem in all_elem:
        div=elem.find_element_by_class_name('img-contain')
        style=div.get_attribute('style')
        image_link=get_down_link(style)
        print(image_link)
        down_links.append(image_link)


if __name__=='__main__':
    chrome = webdriver.Chrome(chrome_path)
    chrome.set_window_position(100, 50)
    chrome.set_window_size(1300, 1000)
    chrome.get(illustration_hot)
    WebDriverWait(chrome,10).until(EC.title_is('插画_画友_哔哩哔哩相簿'))
    print(chrome.title)
    page_down()
    get_all_image_link()
    for down_link in down_links:
        download_image(down_link,get_keep_path(down_link))

    # elem.click()
    # time.sleep(3)
    # chrome.switch_to.window(chrome.window_handles[1])
    # print(chrome.title)
    # time.sleep(3)
    # chrome.close()
    # time.sleep(1)

# chrome.quit()

