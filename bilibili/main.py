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



down_links=[]

chrome=None


# 获取的链接进行转换
def change_down_link(style):
    css='background-size: cover; background-image: url'
    url=style.replace(css,'')[2:-3].split('@')[0]
    return url



# 获取页面下的所有图片下载链接
def get_bili_img():
    bili_imgs=[]
    all_li=chrome.find_elements_by_class_name('a-fade-in')
    for li in all_li:
        detail_link=li.find_element_by_tag_name('a').get_attribute('href')
        img_html=li.find_element_by_class_name('img-contain').get_attribute('style')
        down_link=[get_down_link(img_html)]
        name=[os.path.basename(down_link[0])]
        author=li.find_element_by_tag_name('span').text
        img=bili_img(name,author,detail_link,down_link,1,'','','','','','')
        bili_imgs.append(img)
        # img.print_first()
    return bili_imgs

#
# def open_detail_link(chrome,link):
#     js = "window.open('{0}')".format(link)
#     print('js==='+js)
#     chrome.execute_script(js)

def get_other_info(handle,bili_img):
    chrome.switch_to.window(handle)
    images=chrome.find_element_by_class_name('images')
    imgs=images.find_elements_by_tag_name('img')

    create_date = chrome.find_element_by_class_name('create-date').text.replace('上传时间：', '')
    category = [item.text for item in chrome.find_elements_by_class_name('category')]
    tag=[item.text for item in chrome.find_elements_by_class_name('tag-item')]
    meta_info = chrome.find_element_by_class_name('meta-info').find_elements_by_tag_name('p')
    character_name,source=None,None
    try:
        if len(meta_info)==0:
            character_name = []
            source = []
        elif len(meta_info)==1:
            all_item=[item.text for item in meta_info[0].find_elements_by_tag_name('span')]
            if all_item[0]=='来源：':
                character_name =[]
                source=all_item
            elif all_item[0]=='角色：':
                character_name = all_item
                source = []
        else:
            character_name=[item.text for item in meta_info[0].find_elements_by_tag_name('span')]
            source=[item.text for item in meta_info[1].find_elements_by_tag_name('span')]
    except:
        character_name='get false'
        source='get false'
    discription=chrome.find_element_by_class_name('discription').text
    if len(imgs)==0:
        return
    else:
        for img in imgs:
            down_link=img.get_attribute('data-photo-imager-src')
            name=os.path.basename(down_link)

            # for category in all_category:
            #     print(category.text)

            bili_img.name.append(name)
            bili_img.down_link.append(down_link)
            bili_img.num+=1

    bili_img.create_date=create_date
    bili_img.category=category
    bili_img.tag=tag
    bili_img.discription=discription

    bili_img.character_name=character_name
    bili_img.source=source

    chrome.close()
    bili_img.print_all()
    return bili_img

def download_first_page_image(bili_imgs):
    for img in bili_imgs:
        for (_name,_down_link) in zip(img.name,img.down_link):
            if _name not in os.listdir(image_keep_path):
                print(_name+'   '+_down_link,end='\n')
                download_image_list(_down_link)

if __name__=='__main__':
    bili_imgs=[]
    chrome = webdriver.Chrome(chrome_path)
    chrome.set_window_position(100, 50)
    chrome.set_window_size(1300, 1000)

    # 插画 最热
    chrome.get(illustration_hot)
    time.sleep(3)
    WebDriverWait(chrome,10).until(EC.title_is('插画_画友_哔哩哔哩相簿'))
    # page_down(chrome,30)
    # time.sleep(5)
    bili_imgs=get_bili_img()

    # download_first_page_image(bili_imgs)

    for i in range(0,len(bili_imgs),step):
        tmp_imgs=bili_imgs[i:i+step]
        for img in tmp_imgs:
            js = "window.open(\"{0}\")".format(img.detail_link)
            chrome.execute_script(js)
        time.sleep(3)
        handles = chrome.window_handles

        for (handle,img) in zip(handles[-1:-len(handles):-1],tmp_imgs):
            get_other_info(handle,img)
        time.sleep(3)
        chrome.switch_to.window(handles[0])

    # ============= Test ==============

    #
    # print('--- over ---')
    # chrome.quit()