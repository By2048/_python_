import os
import urllib
import urllib.request
import time
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
        img.print_first()
    return bili_imgs



if __name__=='__main__':
    chrome = webdriver.Chrome(chrome_path)
    chrome.set_window_position(100, 50)
    chrome.set_window_size(1300, 1000)

    # 插画 最热
    chrome.get(illustration_hot)
    time.sleep(3)
    WebDriverWait(chrome,10).until(EC.title_is('插画_画友_哔哩哔哩相簿'))
    page_down(chrome,30)
    bili_imgs=get_bili_img()

    for img in bili_imgs:
        for (_name,_down_link) in zip(img.name,img.down_link):
            if _name not in os.listdir('F:\\- Bilibili2'):
                print(_name+'   '+_down_link,end='\n')
                download_image(_down_link)

    # elem.click()
    # time.sleep(3)
    # chrome.switch_to.window(chrome.window_handles[1])
    # print(chrome.title)
    # time.sleep(3)
    # chrome.close()
    # time.sleep(1)

# chrome.quit()
# js="window.open('http://www.sohu.com')"
# chrome.execute_script(js)
