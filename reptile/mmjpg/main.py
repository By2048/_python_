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
import sqlite3

try:
    from color_print import *
except ImportError:
    from .color_print import *


# 基本环境设置 超时等待时间 下载路径 进程池数量 已经下载的文件路径 浏览器标识
wait_time = 10
socket.setdefaulttimeout(wait_time)
pool_num = multiprocessing.cpu_count() * 3

keep_path = "F:\\Image\\mzt-mmjpg\\"

# os.chdir('mzt-mmjpg')
has_down_path = os.path.abspath('has_down.txt')

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'
headers = {'User-Agent': user_agent}
start_url = 'http://www.mzitu.com/all'


# 连接名字 连接地址
class meizi:
    link = ''
    title=''
    tag=''
    release_time=''
    browse_num = ''
    def __init__(self,  link,title,tag,release_time,browse_num):
        self.link = link
        self.title = title
        self.tag = tag
        self.release_time = release_time
        self.browse_num = browse_num

def init_sql():
    if os.path.isfile('mzt-mmjpg.db'):
        pass
    else:
        cur.execute('''
        create table has_down
        (
            id              integer primary key autoincrement not null,
            link            varchar not null,
            title           nvarchar not null,
            tag             nvarchar not null,
            release_time    text not null,
            browse_num      integer not null
        );
        ''')

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
        imgs = soup.find('div', class_='main-image-test').find_all('img')
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
    time.sleep(5)


def get_has_down_by_sql():
    cur.execute("select * from has_down")
    cnt=0
    has_down_link=[]
    for item in cur.fetchall():
        # cnt+=1
        # item=[str(cnt),str(item[0]),item[1],item[2],item[3],item[4],str(item[5])]
        # print('    '.join(item))
        has_down_link.append(item[1])
    return has_down_link



def keep_has_down_into_sql(info):
    item = [info.link, info.title, info.tag, info.release_time, info.browse_num]
    cur.execute("insert into has_down(link,title,tag,release_time,browse_num) values(?,?,?,?,?)", item)
    conn.commit()

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
        tmp = meizi(link['href'],link.get_text(),'','','')
        meizi_links.append(tmp)
    return meizi_links



#  获取第一张图片的下载地址 根据地址合成下载连接
def get_down_link_list_by_str(first_link, max_num):
    down_links = []
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
    img = soup.find('div', class_='content').find('img')
    return img['src']


def get_other_info(link):
    html = urllib.request.Request(link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    infos = soup.find('div', class_='info').find_all('i')
    title=soup.find('div', class_='article').find('h2').get_text()
    time=infos[0].get_text()[5:]

    tags=soup.find('div', class_='tags')
    tag=','.join([item.get_text() for item in tags.find_all('a')])

    num=infos[3].get_text()[2:][1:-1]

    # print(link+'    '+title+'   '+time+'   '+tag+'   '+num)
    # http://www.mmjpg.com/mm/1051    大胸妹悠悠黑色性感内衣图片无可挑剔   2017年07月20日   美胸,内衣,萌妹   1295841

    for a in soup.find('div', class_='page').find_all('a'):
        if (a.get_text() == '下一张'):
            max_num = a.previous_sibling.previous_sibling.get_text()

    first_img_link = soup.find('div', class_='content').find('img')['src']


    return first_img_link,int(max_num),meizi(link,title,tag,time,num)

def start():
    print('\nStart')

    has_down_list = get_has_down_by_sql()
    max_page_num = get_max_page_num()
    max_page_num = 5
    for page_num in range(int(max_page_num)):
        meizi_links = get_meizi_link_in_one_page(page_num + 1)
        for meizi in meizi_links:
            if meizi.link not in has_down_list:
                printGreen('\n' + 'meizi_index_link  :  ' + meizi.link + '\n')
                printGreen('meizi_index_title :  ' + meizi.title + '\n')

                first_img_link,max_image_num,meizi=get_other_info(meizi.link)

                down_link_list = get_down_link_list_by_str(first_img_link, max_image_num)

                printGreen('image_start_link  :  ' + down_link_list[0] + '\n')
                printGreen('image_max_num     :  ' + str(max_image_num) + '\n')

                print('\n'.join(down_link_list))
                # down_group_img(down_link_list, meizi.title)
                # keep_has_down_into_sql(meizi)
    print('End')


def new_down(link, path):
    response = requests.get(link)
    if response.status_code == 200:
        with open(path, 'wb') as file:
            file.write(response.content)


if __name__ == '__main__':
    conn = sqlite3.connect('mzt-mmjpg.db')
    cur = conn.cursor()

    # a,b,c=get_other_info('http://www.mmjpg.com/mm/1079')
    # print(a)
    # print(str(b))
    # print(c.link)
    # print(c.title)
    # print(c.tag)
    # print(c.browse_num)
    # print(c.release_time)

    # start()

    down_link_list = get_down_link_list_by_str('http://img.mmjpg.com/2017/1080/1.jpg', 41)
    down_group_img(down_link_list, meizi.title)