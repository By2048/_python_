# Time 2017-2-1
import json
import urllib.request
import sys
import os
import shutil

try:
    from .config import *
except ImportError:
    from config import *

class BgImage:
    def __init__(self, enddate, link, title):
        self.enddate = enddate
        self.link = link
        self.title = title

# 下载回显
def call_back(blocknum, blocksize, totalsize):
    # @blocknum: 已经下载的数据块    @blocksize: 数据块的大小    @totalsize: 远程文件的大小
    percent = 100.0 * blocknum * blocksize / totalsize
    sys.stdout.write("\rDownloading : %.2f%%\r" % percent)
    sys.stdout.flush()
    if percent >= 100:
        sys.stdout.write("\rDownloading : %.2f%% -> " % 100)
        print('Download_Success ')

# api detail link = http://stackoverflow.com/questions/10639914/is-there-a-way-to-get-bings-photo-of-the-day
# api = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'
def get_image(idx, n):  # idx=0,n=1
    bing_img_api = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=' + str(idx) + '&n=' + str(n) + '&mkt=en-US'
    bing_json = urllib.request.urlopen(bing_img_api).read().decode('utf-8')
    BgImages = []
    json_data = json.loads(bing_json)
    for i in range(n):
        image_enddate = json_data['images'][i]['enddate']
        image_title = json_data['images'][i]['copyright'].replace('/', ' ')
        image_link = 'http://www.bing.com' + json_data['images'][i]['url']
        BgImages.append(BgImage(image_enddate, image_link, image_title))
    return BgImages

def get_image_name(image):
    image_name=image.enddate[0:4]+"-"+image.enddate[4:6]+"-"+image.enddate[6:8]\
               +" "\
               + image.title \
               + '.' \
               + image.link.split('.')[-1]
    return image_name

def create_temp_jpg(img_path):
    if os.path.exists(img_path)==False:
        with open(img_path, 'w') as file:
            file.close()


if __name__ == '__main__':
    print('\nStart')
    images = get_image(idx=0, n=7)
    image_path=""
    create_temp_jpg(temp_image_path)
    for image in images:
        image_path = image_keep_path + get_image_name(image)
        if os.path.isfile(image_path):
            pass
            # print('\n' + image-test.title + '\n' + image-test.link)
            # print('Has been downloaded')
        else:
            print('\n' + image.title + '\n' + image.link)
            urllib.request.urlretrieve(image.link, image_path,call_back)
            temp_image_path=image_keep_path+"-Temp.jpg"
            shutil.copy(image_path,temp_image_path)
    os.system("start {0}".format(temp_image_path))
    print('\nEnd')