# Coding=utf-8
# Author By2048 Time 2017-7-14
import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
import multiprocessing
import re
import socket
import time
import sys
import requests


try:
    from color_print import *
except ImportError:
    from .color_print import *


# 基本环境设置 超时等待时间 下载路径 进程池数量 已经下载的文件路径 浏览器标识
wait_time = 10
socket.setdefaulttimeout(wait_time)
pool_num = multiprocessing.cpu_count() * 3

keep_path = "F:\\Image\\mzt-mmjpg\\"

os.chdir('mzt-mmjpg') 
has_down_path = os.path.abspath('has_down.txt')

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}
start_url = 'http://www.mzitu.com/all'


# 连接名字 连接地址
class meizi:
    title = ''
    link = ''
    date = ''

    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.date = ''


# # 编码转换 去除非 汉字 英文字符
# def change_coding(inStr):
#     outStr = ""
#     is_zh = re.compile(r"[\u4e00-\u9fff]")
#     is_en = re.compile(r"[A-Za-z]")
#     is_num = re.compile(r"[0-9]")
#     is_spaces = re.compile(r"[\s]+")
#     is_point = re.compile(r".")
#     is_backslash = re.compile(r"\\")
#     is_question_mark = re.compile(r"\?")
#     is_exclamation_point = re.compile(r"! ")
#     try:
#         for word in inStr:
#             if re.match(is_zh, word) != None:
#                 outStr += re.match(is_zh, word).group()
#             elif re.match(is_en, word) != None:
#                 outStr += re.match(is_en, word).group()
#             elif re.match(is_num, word) != None:
#                 outStr += re.match(is_num, word).group()
#             elif re.match(is_spaces, word) != None:
#                 outStr += " "
#             elif re.match(is_backslash, word) != None:
#                 outStr += ""
#             elif re.match(is_point, word) != None:
#                 outStr += ""
#             elif re.match(is_question_mark, word) != None:
#                 outStr += ""
#             elif re.match(is_exclamation_point, word) != None:
#                 outStr += ""
#     except:
#         print("Change_Coding_Fail")
#     finally:
#         if (len(outStr) == 0):
#             return "EmptyName"
#         else:
#             return outStr


# 创建下载文件夹目录文件目录
def create_keep_path(title):
    folder_path = keep_path + title
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


# 根据图片下载连接获取图片名字
def get_image_name(link):
    return link.split('/')[-1]


# 获取图片下载连接 return List  旧页面 存在一个页面两个图片的情况
def get_img_down_link(link):
    html = urllib.request.Request(link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    img_down_link = []
    try:
        imgs = soup.find('div', class_='main-image').find_all('img')
        for img in imgs:
            img_down_link.append(img['src'])
            # print 打开所有连接 在每个连接中获取图片 的情况
            # print('meizi_img_down_link : {0}'.format(img['src']))
            # 根据第一条连接和max_num合成其他连接
            # printGreen('image_start_link  : '+img['src'] + '    \n')
    except:
        print('Get_img_link_fail')
    finally:
        return img_down_link


# 使用进程 获取主页连接下所有的图片下载连接 一个个打开网页
def get_down_link_list(link, max_num):
    pool_resule = []

    pool = multiprocessing.Pool(processes=pool_num)
    for cnt in range(1, max_num + 1):
        detail_link = link + '/' + str(cnt)
        pool_resule.append(pool.apply_async(get_img_down_link, (detail_link,)))
    pool.close()
    pool.join()
    # for tmp in pool_down_link:
    # 	print(tmp)
    # 	tmp_list.append(tmp.get())
    # down_link = [item for sub in tmp_list for item in sub]
    down_link = [item for sub in pool_resule for item in sub.get()]
    return down_link


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
        print("Download_fail " + link + " " + path)


# 下载一组图片 一个连接下所有图片
def down_group_img(img_down_list, title):
    create_keep_path(title)
    pool = multiprocessing.Pool(processes=pool_num)
    for img_down_link in img_down_list:
        down_path = keep_path + title + '\\' + get_image_name(img_down_link)
        pool.apply_async(download, (img_down_link, down_path))
    pool.close()
    pool.join()


# 获取已经下载的连接  has_down.txt -> has_down_list
def get_has_down():
    # file = open(has_down_path, 'r', encoding='utf-8')
    with open(has_down_path, 'r', encoding='utf-8') as file:
    # has_down = [line.strip() for line in file]
        has_down = [line.split('|')[1].strip() for line in file]
    return has_down


# 保存已经下载的链接到
def keep_has_down(meizi):
    has_down_txt = open('has_down.txt', 'a', encoding='utf-8')
    has_down_txt.write(meizi.date + '\t' + '|' + '\t' +
                       meizi.link + '\t' + '|' + '\t' + meizi.title + '\n')
    has_down_txt.close()


# 获取页数  get 共70页  return 70
def get_max_page_num():
    html = urllib.request.Request('http://www.mmjpg.com', headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    hrefs = []
    for em in soup.find('div', class_='page').find_all('em'):
        hrefs.append(em.get_text())
    max_num = hrefs[0]
    return max_num[1:-1]


def get_date(link):
    html = urllib.request.Request(link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    date = soup.find('div', class_='info').find('i').get_text()[5:]
    return date


# 获取开始页面每页的图片的详细连接
def get_meizi_link_in_one_page(page_num):
    page_link = 'http://www.mmjpg.com/home/' + str(page_num)
    html = urllib.request.Request(page_link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    meizi_links = []
    for li in soup.find('div', class_='pic').find('ul').find_all('li'):
        link = li.find('span', class_='title').find('a')
        # tmp = meizi(change_coding(link.get_text()), link['href'])
        tmp = meizi(link.get_text(), link['href'])
        meizi_links.append(tmp)
    return meizi_links


# 获取一个页面的最大图片数量 方便合成连接  40
def get_max_image_num(link):
    html = urllib.request.Request(link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    for a in soup.find('div', class_='page').find_all('a'):
        if (a.get_text() == '下一张'):
            max_num = a.previous_sibling.previous_sibling.get_text()
    return int(max_num)


#  获取第一张图片的下载地址 根据地址合成下载连接
def get_down_link_list_by_str(link, max_num):
    down_links = []
    first_link = get_first_img_down_link(link)
    start_link, image_name = os.path.split(first_link)
    start_str = image_name.split('.')[0][:-2]
    end_num = int(image_name.split('.')[0][-2:])
    image_type = image_name.split('.')[1]
    for num in range(end_num, end_num + max_num):
        down_links.append(start_link + '/' + start_str +
                          str(num) + '.' + image_type)
    return down_links


# 获取图片下载连接 return List  旧页面 存在一个页面两个图片的情况
def get_first_img_down_link(link):
    html = urllib.request.Request(link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    imgs = soup.find('div', class_='content').find('img')
    return imgs['src']


def start():
    print('\nStart')
    has_down_list = get_has_down()
    max_page_num = get_max_page_num()
    max_page_num = 1
    for page_num in range(int(max_page_num)):
        meizi_links = get_meizi_link_in_one_page(page_num + 1)
        for meizi in meizi_links:
            if meizi.link not in has_down_list:
                printGreen('\n' + 'meizi_index_link  :  ' + meizi.link + '\n')
                printGreen('meizi_index_title :  ' + meizi.title + '\n')

                max_image_num = get_max_image_num(meizi.link)
                date = get_date(meizi.link)
                meizi.date = date
                down_link_list = get_down_link_list_by_str(
                    meizi.link, max_image_num)

                printGreen('image_start_link  :  ' + down_link_list[0] + '\n')
                printGreen('image_max_num     :  ' + str(max_image_num) + '\n')

                down_group_img(down_link_list, meizi.title)
                keep_has_down(meizi)
    print('End')


def new_down(link, path):
    response = requests.get(link)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    start()


    # ul='http://www.mmjpg.com/mm/1047'
    # print(get_max_image_num(ul))
    # pp=get_down_link_list_by_str(ul,35)
    #
    # for p in pp:
    #     down_path = keep_path + "-Test" + '\\' + get_image_name(p)
    #     new_down(p, down_path)
