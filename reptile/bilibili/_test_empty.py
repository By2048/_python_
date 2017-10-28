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
    from .tool import *
    from .main import *
    from .config import *
except ImportError:
    from tool import *
    from config import *
    from main import *


link='http://h.bilibili.com/743458'
link_1='http://h.bilibili.com/732450'

chrome=webdriver.Chrome(chrome_path)

chrome.set_window_position(100, 50)
chrome.set_window_size(1300, 1000)
chrome.get(link)

time.sleep(3)

def get_other_info():
    try:
        images = chrome.find_element_by_class_name('images')
        imgs = images.find_elements_by_tag_name('img')
        create_date = chrome.find_element_by_class_name('create-date').text.replace('上传时间：', '')
        category = [item.text for item in chrome.find_elements_by_class_name('category')]
        tag = [item.text for item in chrome.find_elements_by_class_name('tag-item')]
        meta_info = chrome.find_element_by_class_name('meta-info').find_elements_by_tag_name('p')
        discription = chrome.find_element_by_class_name('discription').text

        character_name, source = None, None
        try:
            if len(meta_info) == 0:
                character_name = []
                source = []
            elif len(meta_info) == 1:
                all_item = [item.text for item in meta_info[0].find_elements_by_tag_name('span')]
                if all_item[0] == '来源：':
                    character_name = []
                    source = all_item
                elif all_item[0] == '角色：':
                    character_name = all_item
                    source = []
            else:
                character_name = [item.text for item in meta_info[0].find_elements_by_tag_name('span')]
                source = [item.text for item in meta_info[1].find_elements_by_tag_name('span')]
        except:
            character_name = 'get false'
            source = 'get false'

        if len(imgs) >= 1:
            for img in imgs:
                down_link = img.get_attribute('data-photo-imager-src')
                name = os.path.basename(down_link)
                print('1',end='    ')
                print(down_link)
                print('2',end='    ')
                print(name)
        else:
            pass

        print('3', end='    ')
        print(create_date)
        print('4', end='    ')
        print(category)
        print('5', end='    ')
        print(tag)
        print('6', end='    ')
        print(discription)
        print('7', end='    ')
        print(character_name)
        print('8', end='    ')
        print(source)
    except:
        pass
    finally:
        chrome.close()

get_other_info()



# pp=chrome.find_element_by_class_name('ssr-content').find_elements_by_class_name('empty-hint')
# print(pp)
# print(type(pp))
# print(len(pp))
# print('=============')


# images = chrome.find_element_by_class_name('images')
# imgs = images.find_elements_by_tag_name('img')
#
# print(images)
# print(type(images))
#
# print('=============')
#
# print(imgs)
# print(type(imgs))
# print(len(imgs))