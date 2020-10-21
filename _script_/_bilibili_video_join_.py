import logging
import os
import json
import shutil
from pprint import pprint

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)1.1s %(lineno)3d] %(message)s',
    datefmt='%H:%M:%S'
)

ffmpeg_path = "D:\\FFmpeg\\bin\\ffmpeg.exe"
download_path = "T:\\bilibili\\"
keep_path = "T:\\"

# bilibili (download_path)
# ├─xxxxxxxx (collection)
# │  ├─1 (video1)
# │  └─2 (video2)
# ├─xxxxxxxx
# │  └─1


logging.info("\n")
logging.info(f'ffmpeg_path      {ffmpeg_path}')
logging.info(f'download_path    {download_path}')
logging.info(f'keep_path        {keep_path}')
logging.info("\n")


class Video(object):
    def __init__(self, folder_path, title=""):
        self.folder_path = folder_path
        self.title = title

    def __repr__(self):
        return f"path:{self.folder_path} | title:{self.title}"


def get_all_video():
    videos = []
    for collection_folder in os.listdir(download_path):
        collection_folder_path = os.path.join(download_path, collection_folder)
        for video_folder in os.listdir(collection_folder_path):
            video_folder_path = os.path.join(collection_folder_path, video_folder)
            video = Video(folder_path=video_folder_path)
            videos.append(video)
    return videos


def init_video_title(video):
    def change(name):
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
            from hanziconv import HanziConv
            # https://pypi.org/project/hanziconv/  简繁体转换
            name = HanziConv.toSimplified(name)
        except ImportError:
            pass
        return name

    # 1 / 2 / xx
    json_file_path = os.path.join(video.folder_path, 'entry.json')
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        title = data['title']
        title = change(title)
        video.title = title

    # if num != 1:
    #     video_name = f"{data['title']}_{data['page_data']['part']}"

    # if data.get('ep', ''):
    #     index = data['ep']['index']
    #     index_title = data['ep']['index_title']
    #     video_name = data['title'] + '_' + index
    #     if index_title:
    #         video_name = data['title'] + '_' + index + '_' + index_title
    #     video_name = change_name(video_name)
    #     return video_name


def move_m4s(video):
    for root, dirs, files in os.walk(video.folder_path):
        for file in files:
            if file.endswith(".m4s"):
                print(os.path.join(root, file))
                try:
                    shutil.move(os.path.join(root, file), video.folder_path)
                except shutil.Error:
                    logging.error(os.path.join(root, file))


def get_join_video(video: Video):
    # 使用 ffmpeg 拼接视频
    video_m4s = os.path.join(video.folder_path, "video.m4s")
    audio_m4s = os.path.join(video.folder_path, "audio.m4s")
    video_output = os.path.join(keep_path, video.title)

    cmd = f" {ffmpeg_path} " \
          f" -i {video_m4s} -i {audio_m4s} " \
          f" -c:v copy " \
          f" -strict experimental " \
          f" {video_output}.mp4 "
    logging.info(cmd)
    os.system(cmd)


def test():
    videos = get_all_video()
    for video in videos:
        init_video_title(video)
        move_m4s(video)
        get_join_video(video)
    pprint(videos)


def setup():
    videos = get_all_video()
    for video in videos:
        init_video_title(video)
        move_m4s(video)
        get_join_video(video)
        print(video)


if __name__ == '__main__':
    # test()
    setup()
