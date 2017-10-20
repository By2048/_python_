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


image_keep_path = "F:\\- Bilibili"
start_url = 'http://h.bilibili.com/eden/draw_area#/all/hot'
chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}

down_links=[]


chrome=None



# 下载回显
def call_back(blocknum, blocksize, totalsize):
    # @blocknum: 已经下载的数据块    @blocksize: 数据块的大小    @totalsize: 远程文件的大小
    percent = 100.0 * blocknum * blocksize / totalsize
    sys.stdout.write("\rDownloading : %.2f%%\r" % percent)
    sys.stdout.flush()
    if percent >= 100:
        sys.stdout.write("\rDownloading : %.2f%% -> " % 100)
        print('Download_Success ')
# 下载图片
def download(link, path):
    try:
        urllib.request.urlretrieve(link, path, call_back)
    except:
        pass

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

def get_keep_path(down_link):
    name = os.path.basename(down_link)
    keep_path=os.path.join(image_keep_path, name)
    keep_path.replace(' ','')
    return keep_path

if __name__=='__main__':
    chrome = webdriver.Chrome(chrome_path)
    chrome.set_window_position(100, 50)
    chrome.set_window_size(1300, 1000)
    chrome.get(start_url)
    WebDriverWait(chrome,10).until(EC.title_is('全部_画友_哔哩哔哩相簿'))
    print(chrome.title)
    page_down()
    get_all_image_link()
    for down_link in down_links:
        download(down_link,get_keep_path(down_link))

    # elem.click()
    # time.sleep(3)
    # chrome.switch_to.window(chrome.window_handles[1])
    # print(chrome.title)
    # time.sleep(3)
    # chrome.close()
    # time.sleep(1)

# chrome.quit()

