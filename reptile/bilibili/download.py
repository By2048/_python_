import os
import urllib
import urllib.request
import sys

try:
    from conf import *
except ImportError:
    from .config import *


def get_keep_path(down_link):
    name = os.path.basename(down_link)
    keep_path=os.path.join(image_keep_path, name)
    keep_path.replace(' ','')
    return keep_path

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

def download_image_list(links):
    for link in links:
        download_image(link)


def download_image(link):
    try:
        urllib.request.urlretrieve(link, get_keep_path(link), call_back)
    except:
        print('download_error   ' + link)