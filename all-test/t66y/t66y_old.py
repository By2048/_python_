# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import os
import sys
import string
import multiprocessing
import socket
from bs4 import BeautifulSoup

# chcp 936(gbk) 65001(utf-8)

socket.setdefaulttimeout(9)

begin_url = 'http://c6.d7w.biz/'
url_1 = "http://c6.d7w.biz/thread0806.php?fid=8"  # 新時代的我們 page?

t66y_name = []
t66y_link = []

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}
html = urllib2.Request(url_1, headers=headers)
response = urllib2.urlopen(html).read()
soup = BeautifulSoup(response, "html.parser", from_encoding="gb2312")

links_1 = soup.find_all('a', href=re.compile(r"htm_data/\d+/\d+/\d+.html"), attrs={"target": "_blank"})

t66y_info = open("O://Download//t66y_info.txt", "w")


# --------------------------------------------------------------------------------------


def get_start_link(id, page):
    t66y_url = 'http://dz.ek9.biz'
    url_1 = "/thread0806.php?fid=7"  # 技术讨论区           id==1
    url_2 = "/thread0806.php?fid=8"  # 新時代的我們         id==2
    url_3 = "/thread0806.php?fid=16"  # 达盖尔的旗帜         id==3
    page_url = "&search=&page="
    page_num = page
    if (id == 1):
        return t66y_url + url_1 + page_url + str(page_num)
    elif (id == 2):
        return t66y_url + url_2 + page_url + str(page_num)
    elif (id == 3):
        return t66y_url + url_3 + page_url + str(page_num)


num = 0


def get_img_keep_path():
    global num
    num += 1
    path = "O:\\Download\\Image\\" + str(num) + ".jpg"
    return path


def call_back(blocknum, blocksize, totalsize):
    '''回调函数
    @blocknum: 已经下载的数据块
    @blocksize: 数据块的大小
    @totalsize: 远程文件的大小
    '''
    percent = 100.0 * blocknum * blocksize / totalsize
    if percent >= 100:
        percent = 100
        # print "%.2f%%"% percent
        print("Download_Success")


def down_img(url, path):
    urllib.urlretrieve(url, path, call_back)


def get_img_link(url):
    img_link = []
    html = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(html).read()
    soup = BeautifulSoup(response, "html.parser", from_encoding="gb2312")
    for input in soup.find_all('input', type="image-test"):
        img = input['src']
        img_link.append(img)
    return img_link


def keep_all_image(img_link):
    pool_num = multiprocessing.cpu_count() * 2
    my_pool = multiprocessing.Pool(pool_num)
    for link in img_link:
        path = get_img_keep_path()
        my_pool.apply_async(down_img, (link, path,))
        #  my_pool.close()


for link in links_1:
    if (link.get_text() != ".::"):
        tmp1 = begin_url + link['href']
        tmp2 = link.get_text()

        tmp1 = tmp1.encode('utf-8')
        tmp2 = tmp2.encode('utf-8')

        t66y_link.append(tmp1)
        t66y_name.append(tmp2)

        t66y_info.writelines(tmp1)
        t66y_info.writelines('\n')
        t66y_info.writelines(tmp2)
        t66y_info.writelines('\n')
        t66y_info.writelines('\n')

t66y_info.close()

if __name__ == "__main__":
    for i in t66y_link:
        print(i)
        img_link_tmp = get_img_link(i)
        keep_all_image(img_link_tmp)

    cmd = "start O:\\download\\t66y_info.txt"
    os.system(cmd)
