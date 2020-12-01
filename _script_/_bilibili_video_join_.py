import logging
import os
import json
import shutil
import subprocess
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)1.1s %(lineno)3d] %(message)s',
    datefmt='%H:%M:%S'
)

base_folder = "T:\\com.bilibili.app.in\\"
ffmpeg_path = "D:\\FFmpeg\\bin\\ffmpeg.exe"
download_path = "T:\\com.bilibili.app.in\\download\\"
keep_path = "T:\\"

"""
bilibili (download_path)
├─xxxxxxxx (Collection)
│  ├─1 (video1)
|  |  |-80
|  |  |  audio.m4s
│  |  |  index.json
│  |  |  video.m4s
|  |  |-64
|  |  |  audio.m4s
│  |  |  index.json
│  |  |  video.m4s
│  |  danmaku.xml
│  │  entry.json

80 64 指不同分辨率
一般来说只保留一个 越大越好
处理时如果存在多个删除小的
"""

logging.info('')
logging.info('-' * 66)
logging.info(f'ffmpeg_path      {ffmpeg_path}')
logging.info(f'download_path    {download_path}')
logging.info(f'keep_path        {keep_path}')
logging.info('-' * 66)


class Video(object):
    def __init__(self, folder="", index=0, part="", title=""):
        self.folder = folder
        self.index = index
        self.part = part
        self.title = title
        self.files = []

    def __str__(self):
        result = f"{'-> video_index'.rjust(20)} {self.index}\n"
        result += f"{' video_part'.rjust(28)} {self.part}\n"
        result += f"{'video_title'.rjust(28)} {self.title}"
        return result


class Collection(object):
    def __init__(self, folder):
        self.folder: str = folder
        self.videos: [Video] = []

    @property
    def count(self):
        return len(os.listdir(self.folder))

    def __str__(self):
        result = f"{'collection_path'.rjust(20)} {self.folder}"
        return result


def init_collections():
    collections = []

    for collection_folder in os.listdir(download_path):
        collection_folder_path = os.path.join(download_path, collection_folder)
        collection = Collection(folder=collection_folder_path)
        videos = []
        for video_folder in os.listdir(collection_folder_path):
            video_folder_path = os.path.join(collection_folder_path, video_folder)
            video = Video(folder=video_folder_path, index=int(video_folder))
            videos.append(video)
        collection.videos = videos
        logging.info(collection)
        collections.append(collection)

    logging.info('-' * 66)
    logging.info('')
    logging.info('')

    return collections


def change_name(name):
    codes = [
        # ('?', ''),
        # ('？', ''),
        # ('，', '')
        # ('》', ''),
        # ('| ', ''),
        # ('*', ''),
        # (' ', '_'),
        # ('\\', '_'),
        # ('/', '_'),
        # ('【', '['),
        # ('】', ']'),
        # ('《', ''),
    ]
    for item in codes:
        name = name.replace(item[0], item[1])
    try:
        # https://pypi.org/project/hanziconv/  简繁体转换
        from hanziconv import HanziConv
        name = HanziConv.toSimplified(name)
    except ImportError:
        pass
    return name


def init_collection_videos(collection: Collection):
    for video in collection.videos:
        json_file_path = os.path.join(video.folder, 'entry.json')  # 视频信息

        # 删除较小分辨率的视频
        video_resolution_items = os.listdir(video.folder)
        video_resolution_items.remove('danmaku.xml')
        video_resolution_items.remove('entry.json')
        if len(video_resolution_items) > 1:
            _item_ = sorted(video_resolution_items, key=lambda x: int(x))
            video_resolution_min = os.path.join(video.folder, _item_[0])
            shutil.rmtree(video_resolution_min)

        # 初始化视频文件
        video_file_folder = video_resolution_items[-1]
        video_file_folder = os.path.join(video.folder, video_file_folder)
        for video_file in os.listdir(video_file_folder):
            if video_file.endswith('.json'):
                continue
            video.files.append(os.path.join(video_file_folder, video_file))

        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            part = data['page_data']['part']
            title = data['title']
            part = change_name(part)
            title = change_name(title)
            video.part = part
            video.title = title
        # logging.info(video)

    # if data.get('ep', ''):
    #     index = data['ep']['index']
    #     index_title = data['ep']['index_title']
    #     video_name = data['title'] + '_' + index
    #     if index_title:
    #         video_name = data['title'] + '_' + index + '_' + index_title
    #     video_name = change_name(video_name)
    #     return video_name


def join_video(video: Video):
    # 使用 ffmpeg 拼接视频

    if len(video.files) < 2:
        logging.error('')
        logging.error('')
        logging.info('-' * 66)
        logging.error(f"下载文件缺失")
        logging.error(f"\t{video.title}")
        logging.error(f"\t{video.folder}")
        logging.error(f"\t{str(video.files)}")
        logging.info('-' * 66)
        logging.error('')
        logging.error('')
        return

    logging.info('-' * 66)

    video_m4s = video.files[0]
    audio_m4s = video.files[1]
    if "video" not in video_m4s or "audio" not in audio_m4s:
        video_m4s, audio_m4s = audio_m4s, video_m4s

    names = {
        "1": f"{video.title}",
        "2": f"{video.part}",
        "3": f"{video.title} {video.part}",
        "4": f"{video.index} {video.title} {video.part}",
        "5": f"{datetime.now().strftime('%Y-%m-%d')} {video.title}",
    }

    data = "#选项# \n"
    for key, value in names.items():
        data += f"\t\t[#{key}] {value}\n"
    data = data.rstrip("\n")
    logging.info(data)

    check = None
    while True:
        check = input(" #选择# ".rjust(13))
        if check:
            break

    check = "1" if check == "\\" else check
    if check not in names.keys():
        return

    name = names.get(check)
    if not name:
        return

    video_output = os.path.join(keep_path, name)

    cmd = f" {ffmpeg_path} " \
          f" -i {video_m4s} -i {audio_m4s} " \
          f" -c:v copy " \
          f" -strict experimental " \
          f" \"{video_output}.mp4\" "
    logging.info('-' * 66)
    logging.info(cmd)
    logging.info('-' * 66)
    os.system(cmd)
    # subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)


def clear():
    check = input("\n\n\n #删除下载文件夹# \n\n\n \t\t\t")
    if check in ['1', 'y', '\\']:
        shutil.rmtree(base_folder)
    print()
    print()


def test():
    pass


def setup():
    if not os.path.exists(base_folder):
        logging.error(f"不存在路径 {base_folder}")
        return

    collections = init_collections()
    for collection in collections:
        init_collection_videos(collection)
        for video in collection.videos:
            join_video(video)

    clear()


if __name__ == '__main__':
    setup()
    # test()
