import sys
import urllib.request
import sys
import os

down_link=r'ftp://ygdy8:ygdy8@y219.dydytt.net:9245/[%E9%98%B3%E5%85%89%E7%94%B5%E5%BD%B1www.ygdy8.com].%E6%80%AA%E7%89%A9%E5%8F%AC%E5%94%A4.BD.720p.%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97%E5%B9%95.mkv'
down_path=r'f:\怪物召唤.mkv'
def call_back(blocknum, blocksize, totalsize):
    # @blocknum: 已经下载的数据块    @blocksize: 数据块的大小    @totalsize: 远程文件的大小
    percent = 100.0 * blocknum * blocksize / totalsize
    sys.stdout.write("\rDownloading : %.2f%%\r"% percent)
    sys.stdout.flush()
    if percent >= 100:
        sys.stdout.write("\rDownloading : %.2f%% -> " % 100)
        print('Download_Success ')


urllib.request.urlretrieve(down_link, down_path, call_back)