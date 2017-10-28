# Coding=utf-8
# Author By2048 Time 2017-1-18
import os
import sys
import urllib
import urllib.request
from bs4 import BeautifulSoup
import multiprocessing
import re
import socket
from tqdm import tqdm
from time import sleep
import multiprocessing


# 下载回显
def call_back(blocknum, blocksize, totalsize):
    # @blocknum: 已经下载的数据块    @blocksize: 数据块的大小    @totalsize: 远程文件的大小
    percent = 100.0 * blocknum * blocksize / totalsize
    sys.stdout.write("\rDownloading : %.2f%%\r"% percent)
    sys.stdout.flush()
    if percent >= 100:
        sys.stdout.write("\rDownloading : %.2f%% -> " % 100)
        print('Download_Success ')

# 下载图片
def download(link,path):
    urllib.request.urlretrieve(link,path,call_back)

# for i in tqdm(range(1,3)):
#     kk = download(link, path)
#     if(kk==True):
#         sleep(1)
if __name__=="__main__":
    link = "http://ossweb-img.qq.com/images/lol/web201310/skin/big99007.jpg"
    link_1="https://d.ruanmei.com/tweakcube/partner/pcmastersetup_u12_full.exe"
    path = "E:\\Desktop\\big99007.jpg"
    path_1 = "E:\\Desktop\\Pcmaster.exe"
    # download(link,path)
    download(link_1,path_1)