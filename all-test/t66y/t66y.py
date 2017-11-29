# encoding : utf-8

import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
import multiprocessing
import sys
import time
import re

# 初始化 定义基本环境变量

pool_num = multiprocessing.cpu_count()
sleep_time = 5
t66y_path = "F:\\Image\\t66y\\"
start_url = 'http://c6.zh4.co//'
fid8 = start_url + '/thread0806.php?fid=8&search=&page=1'  # 新时代的我们
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}

# mathch_1="src='http://.*?.jpg'"   #Img
# mathch_2="htm_data/\d+/\d+/\d+.html"    #link

class Img:
    title = ""
    link = ""
    def __init__(self, title, link):
        self.title = title
        self.link = link

# 编码转换 去除非 汉字 英文字符
def change_coding(inStr):
    outStr = ""
    is_zh = re.compile(r"[\u4e00-\u9fff]")
    is_en = re.compile(r"[A-Za-z]")
    is_num = re.compile(r"[0-9]")
    is_spaces = re.compile(r"[\s]+")
    is_point = re.compile(r".")
    is_backslash = re.compile(r"\\")
    is_question_mark = re.compile(r"\?")
    is_exclamation_point = re.compile(r"! ")
    try:
        for word in inStr:
            if re.match(is_zh, word) != None:
                outStr += re.match(is_zh, word).group()
            elif re.match(is_en, word) != None:
                outStr += re.match(is_en, word).group()
            elif re.match(is_num, word) != None:
                outStr += re.match(is_num, word).group()
            elif re.match(is_spaces, word) != None:
                outStr += " "
            elif re.match(is_backslash, word) != None:
                outStr += ""
            elif re.match(is_point, word) != None:
                outStr += ""
            elif re.match(is_question_mark, word) != None:
                outStr += ""
            elif re.match(is_exclamation_point, word) != None:
                outStr += ""
    except:
        print("Change_Coding_Fail")
    finally:
        if (len(outStr) == 0):
            return "EmptyName"
        else:
            return outStr


# 创建下载文件夹目录文件目录
def create_keep_path(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# 获取一页所有链接
def get_image_link(url):
    images=[]
    html = urllib.request.Request(url, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser",from_encoding="gb2312")
    all_link = soup.find_all('tr', class_='tr3 t_one tac')
    for link in all_link:
        aLink = link.find('h3').find('a')
        title = change_coding(aLink.get_text())
        link = start_url+aLink['href']
        images.append(Img(title, link))
    return images


def get_image_down_link(link):
    down_links=[]
    html = urllib.request.Request(link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser", from_encoding="GBK")
    try:
        inputs=soup.find_all('input', type="image")
        for input in inputs:
            down_link=input['src']
            down_links.append(down_link)
    except:
        down_links.append('')
    return down_links

# 下载回显
def call_back(blocknum, blocksize, totalsize):
    # @blocknum: 已经下载的数据块    @blocksize: 数据块的大小    @totalsize: 远程文件的大小
    percent = 100.0 * blocknum * blocksize / totalsize
    sys.stdout.write("\rDownloading : %.2f%%\r" % percent)
    sys.stdout.flush()
    if percent >= 100:
        sys.stdout.write("\rDownloading : %.2f%% -> " % 100)
        print('Download_Success ')

def download(link, path):
    try:
        urllib.request.urlretrieve(link, path, call_back)
    except:
        pass

def get_image_name(url):
    return url.split('/')[-1]

def get_has_down():
    file = open('has_down.txt', 'r')
    has_down = [line.split('<|>')[0].strip() for line in file]
    return has_down

def keep_has_down(image):
    has_down_txt = open('has_down.txt', 'a')
    has_down_txt.write(image.link + '\t' + '<|>' + '\t' + change_coding(image.title) + '\n')
    has_down_txt.close()

if __name__ == '__main__':
    print('Start')
    has_downs = get_has_down()
    images=get_image_link('http://c6.zh4.co/thread0806.php?fid=8&search=&page=1')
    for image in images[9:]:
        print(image.link)
        if image.link not in has_downs:
            folder_path = t66y_path + image.title+ '\\'
            create_keep_path(folder_path)
            down_links=get_image_down_link(image.link)
            for down_link in down_links:
                down_path=folder_path+get_image_name(down_link)
                download(down_link,down_path)
            keep_has_down(image)
            print('\n-------------------------- Sleep(5) --------------------------\n')
            time.sleep(5)
