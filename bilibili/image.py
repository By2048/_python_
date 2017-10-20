import os
import urllib
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


image_keep_path = "F:\\- Bilibili"
start_url = 'http://h.bilibili.com/eden/draw_area#/all/hot'
chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}


chrome = webdriver.Chrome(chrome_path)
chrome.set_window_position(50,50)
chrome.set_window_size(1300,1000)
chrome.get(start_url)


# WebDriverWait(chrome,10).until(EC.title_is('全部_画友_哔哩哔哩相簿'))
time.sleep(3)
print(chrome.title)


# 获取的链接进行转换
def get_image_link(style):
    css='background-size: cover; background-image: url'
    url=style.replace(css,'')[2:-3].split('@')[0]
    return url


# PageDown 模块
def page_down():
    for i in range(9):
        print('page down ...')
        ActionChains = webdriver.common.action_chains.ActionChains
        ActionChains(chrome).send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(3)

# 获取页面下的所有图片下载链接
def get_all_image_link():
    all_elem=chrome.find_elements_by_class_name('a-fade-in')
    for elem in all_elem:
        div=elem.find_element_by_class_name('img-contain')
        style=div.get_attribute('style')
        image_link=get_image_link(style)
        print(image_link)
if __name__=='__main__':
    pass


    # elem.click()
    # time.sleep(3)
    # chrome.switch_to.window(chrome.window_handles[1])
    # print(chrome.title)
    # time.sleep(3)
    # chrome.close()
    # time.sleep(1)

# chrome.quit()

