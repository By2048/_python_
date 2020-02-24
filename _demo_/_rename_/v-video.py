user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}

import os
import urllib
import urllib.request
from bs4 import BeautifulSoup

page_link = r'https://www.vmovier.com/'
folder_path = r'F:\\Phone\\V电影\\'


# 视频 id    视频具体路径    视频原名    视频新名
class VVideo(object):
    def __init__(self, id, path, newname):
        self.id = id
        self.path = path
        self.newname = newname


# 根据电影的 id 访问电影的网站获取电影名
def get_name(video_id):
    _link = r'https://www.vmovier.com/' + video_id
    html = urllib.request.Request(_link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    name = soup.find('h1', class_='post-title').get_text()
    name = name.replace(' ', '').replace('\n', '')
    return name


if __name__ == '__main__':
    all_vvideo = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.mp4'):
                _path = os.path.join(root, file)
                _id = os.path.split(_path)[0].split('\\')[-1]
                _real_name = get_name(_id)
                tmp = VVideo(id=_id, path=_path, newname=_real_name)
                all_vvideo.append(tmp)

    for item in all_vvideo:
        new_path = folder_path + item.newname + '.mp4'
        os.rename(item.path, new_path)
        print('rename move ' + new_path)
