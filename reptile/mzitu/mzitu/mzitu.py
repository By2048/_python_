# Coding=utf-8
# Author By2048 Time 2017-1-18
import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
import multiprocessing
import re
import socket
import sys
import time
import requests

try:
    from color_print import *
    from config import *
    from sql import *
    from pymysql import *
    from download import *
    from tool import *
    from all_class import *
except ImportError:
    from .color_print import *
    from .config import *
    from .sql import *
    from .download import *
    from .tool import *
    from .all_class import *


# 获取一个页面的最大图片数量 方便合成连接
def get_max_image_num(soup):
    max_num = 0
    for span in soup.find('div', class_='pagenavi').find_all('span'):
        if (span.get_text() == '下一页»'):
            max_num = span.parent.previous_sibling.find('span').get_text()
    return int(max_num)


# 获取图片下载连接 return List  旧页面 存在一个页面两个图片的情况
def get_img_down_link_list(soup):
    img_down_link = []
    try:
        imgs = soup.find('div', class_='main-image').find_all('img')
        for img in imgs:
            img_down_link.append(img['src'])
    except:
        print('Get_img_link_fail')
    finally:
        return img_down_link


# 获取图片的 分类 日期
def get_categroy_and_date(soup):
    all_span = soup.find('div', class_='main-meta').find_all('span')
    category = all_span[0].find('a').get_text()
    date = all_span[1].get_text().replace('发布于 ', '')
    return category, date


def get_other_info_in_detail_link(link):
    html = urllib.request.Request(link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    max_num = get_max_image_num(soup)
    first_down_link = get_img_down_link_list(soup)[0]
    category, date = get_categroy_and_date(soup)
    return max_num, first_down_link, category, date


# 使用进程 获取主页连接下所有的图片下载连接
def get_down_link_list(link, max_num):
    pool_resule = []
    pool = multiprocessing.Pool(processes=pool_num)
    for cnt in range(1, max_num + 1):
        detail_link = link + '/' + str(cnt)
        pool_resule.append(pool.apply_async(get_img_down_link_list, (detail_link,)))
    pool.close()
    pool.join()
    # for tmp in pool_down_link:
    # 	print(tmp)
    # 	tmp_list.append(tmp.get())
    # down_link = [item for sub in tmp_list for item in sub]
    down_link = [item for sub in pool_resule for item in sub.get()]
    return down_link


#  获取第一张图片的下载地址 根据下载地址合成其他下载连接
def get_down_link_list_by_str(first_down_link, max_num):
    """
    http://i.meizitu.net/2017/10/29c02.jpg
    start_link   http://i.meizitu.net/2017/10
    image_name   29c02.jpg
    start_str    29c
    end_num      02
    image_type   jpg
    """
    start_link, image_name = os.path.split(first_down_link)
    start_str = image_name.split('.')[0][:-2]
    end_num = int(image_name.split('.')[0][-2:])
    image_type = image_name.split('.')[1]

    down_link_list = []
    for num in range(end_num, end_num + max_num):
        down_link_list.append(start_link + '/' + start_str + str(num).zfill(2) + '.' + image_type)
    return down_link_list


# 获取 all_img_page 下所有的信息 title link
def get_all_meizi():
    html = urllib.request.Request(all_img_page, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")

    all_meizi = []
    for ul in soup.find_all('ul', class_='archives'):
        for link in ul.find_all('a'):
            mz = meizi_img(change_coding(link.get_text()), link['href'], '', '')
            all_meizi.append(mz)
    return all_meizi


# 获取主页的页数
def get_max_page_num():
    html = urllib.request.Request(start_page, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    all_link = soup.find('div', class_='nav-links').find_all('a')
    num = all_link[-2]['href'].split('/')[-2]
    return int(num)


# 获取开始页面每页中所有的图片的详细连接
def get_meizi_link_in_start_page(page_num):
    page_link = 'http://www.mzitu.com/page/' + str(page_num)
    html = urllib.request.Request(page_link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    meizi_links = []
    for li in soup.find('ul', id='pins').find_all('li'):
        link = li.find('span').find('a')
        tmp = meizi_img(change_coding(link.get_text()), link['href'])
        meizi_links.append(tmp)
    return meizi_links


# 主程序
def start_mzitu():
    print('\nStart')
    has_down_list = get_has_down_by_txt()
    """
    # 使用主页下载图片
    max_page_num=get_max_page_num()
    max_page_num = 5
    for page_num in range(max_page_num):
        meizi_links = get_meizi_link_in_start_page(page_num + 1)
    """
    all_meizi = get_all_meizi()
    for meizi in all_meizi:
        if meizi.link not in has_down_list:
            printGreen('meizi_index_title :  ' + meizi.title + '\n')
            printGreen('meizi_index_link  :  ' + meizi.link + '\n')

            max_num, first_down_link, category, date = get_other_info_in_detail_link(meizi.link)
            meizi.category = category
            meizi.date = date
            down_link_list = get_down_link_list_by_str(first_down_link, max_num)

            printGreen('image_start_link  :  ' + down_link_list[0] + '\n')
            printGreen('image_max_num     :  ' + str(max_num) + '\n')

            down_image_list(down_link_list, meizi.title)

            # 以下载信息数据库保存部分
            # insert_sql_has_down(sql_server_con_text,meizi)
            # down_folder_path = keep_path + meizi.title
            # insert_sql_download_file(sql_server_con_text,down_folder_path)

            time.sleep(9)

            keep_has_down_to_txt(meizi)
            print()
    print('End')

if __name__ == '__main__':
    # start_mzitu()
    for item in get_all_meizi():
        print(item.link)
        print(item.title)
        create_keep_path(item.title)

