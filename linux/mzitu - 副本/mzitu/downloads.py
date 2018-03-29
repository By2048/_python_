import urllib
import urllib.request
import os
import requests
import random
import sqlite3
from contextlib import closing


from config import *


# 创建下载文件夹目录文件目录
def create_keep_path(id):
    folder_path = os.path.join(keep_path, id)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    else:
        print(id + ' has exit')


# 设置请求头
def get_header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) ' +
                       'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                       'Chrome/59.0.3071.115 Safari/537.36'),
        'Accept': 'image-test/webp,image-test/apng,image-test/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers


# 使用reqursts下载图片
def down_image_list(down_link_list, id):
    create_keep_path(id)
    for down_link in down_link_list:
        file_path = os.path.join(keep_path, id, os.path.basename(down_link))
        print('Download   ' + down_link)
        with open(file_path, "wb+") as file:
            file.write(requests.get(down_link, headers=get_header(down_link)).content)


def test():
    head = get_header('qwe')
    print(head)

if __name__ == '__main__':
    test()
