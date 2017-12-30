import urllib
import urllib.request
import os
import requests
import sqlite3
from contextlib import closing
import progressbar

try:
    from color_print import *
    from config import *
except ImportError:
    from .color_print import *
    from .config import *


# 创建下载文件夹目录文件目录
def create_keep_path(title):
    folder_path = keep_path + title
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        print(title + ' exit ------')


# 下载图片
def download_image(link, path):
    try:
        urllib.request.urlretrieve(link, path, call_back)
    except:
        pass
        # print("Download_fail "+link+" "+path )


# 下载回显
def call_back(blocknum, blocksize, totalsize):
    # @blocknum: 已经下载的数据块    @blocksize: 数据块的大小    @totalsize: 远程文件的大小
    percent = 100.0 * blocknum * blocksize / totalsize
    sys.stdout.write("\rDownloading : %.2f%%\r" % percent)
    sys.stdout.flush()
    if percent >= 100:
        sys.stdout.write("\rDownloading : %.2f%% -> " % 100)
        print('Download_Success ')


# 下载一组图片 一个连接下所有图片
def down_group_img(img_down_list, title):
    create_keep_path(title)
    pool = multiprocessing.Pool(processes=pool_num)
    for img_down_link in img_down_list:
        down_path = keep_path + title + '\\' + os.path.basename(img_down_link)
        pool.apply_async(download_image, (img_down_link, down_path))
    pool.close()
    pool.join()



def keep_has_down_to_sqlite(meizi):
    conn = sqlite3.connect(has_down_sql_path)
    cur = conn.cursor()
    cur.execute("INSERT INTO has_down (link,title,category,date)"
                "VALUES ('{0}','{1}','{2}','{3}')"
                .format(meizi.link, meizi.title, meizi.category, meizi.date))
    conn.commit()

def get_has_down_by_sqlite():
    conn = sqlite3.connect(has_down_sql_path)
    cur = conn.cursor()
    cur.execute("SELECT link FROM has_down")
    has_down=[]
    for item in cur.fetchall():
        has_down.append(item[0])
    return has_down


# 设置请求头
def get_header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/59.0.3071.115 Safari/537.36',
        'Accept': 'image-test/webp,image-test/apng,image-test/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers


# 使用reqursts下载图片
def down_image_list(down_link_list, title):
    create_keep_path(title)
    for down_link in down_link_list:
        down_path = keep_path + title + '\\' + os.path.basename(down_link)
        print('Download   ' + down_link)
        with open(down_path, "wb+") as file:
            file.write(requests.get(down_link, headers=get_header(down_link)).content)
