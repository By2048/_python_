import logging
import os
import json
import shutil

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)1.1s %(lineno)3d] %(message)s',
    datefmt='%H:%M:%S'
)

ffmpeg_path = "D:\\FFmpeg\\bin\\ffmpeg.exe"
download_path = "T:\\com.bilibili.app.in\\download\\"
keep_path = "T:\\"

# bilibili (download_path)
# ├─xxxxxxxx (Collection)
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
    def __init__(self, folder="", index=0, part="", title=""):
        self.folder = folder
        self.index = index
        self.part = part
        self.title = title


class Collection(object):
    def __init__(self, folder):
        self.folder: str = folder
        self.videos: [Video] = []

    @property
    def parts_count(self):
        return len(os.listdir(self.folder))

    def __repr__(self):
        result = f"  collection_path {self.folder} \n\n"
        for video in self.videos:
            result += f"      video_index {video.index}\n" \
                      f"       video_part {video.part}\n" \
                      f"      video_title {video.title}\n\n"
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
        collections.append(collection)

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
        from hanziconv import HanziConv
        # https://pypi.org/project/hanziconv/  简繁体转换
        name = HanziConv.toSimplified(name)
    except ImportError:
        pass
    return name


def init_collection_videos(collection: Collection):
    for video in collection.videos:
        # 1 / 2 / xx
        json_file_path = os.path.join(video.folder, 'entry.json')
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            part = data['page_data']['part']
            title = data['title']
            part = change_name(part)
            title = change_name(title)
            video.part = part
            video.title = title

    # if data.get('ep', ''):
    #     index = data['ep']['index']
    #     index_title = data['ep']['index_title']
    #     video_name = data['title'] + '_' + index
    #     if index_title:
    #         video_name = data['title'] + '_' + index + '_' + index_title
    #     video_name = change_name(video_name)
    #     return video_name


def move_m4s(video: Video):
    for root, dirs, files in os.walk(video.folder):
        for file in files:
            if file.endswith(".m4s"):
                _1_ = os.path.join(root, file)
                _2_ = video.folder
                try:
                    shutil.move(os.path.join(root, file), video.folder)
                    logging.info(f"  {_1_} \n        ->{_2_}")
                except shutil.Error:
                    logging.error(f"  {_1_} \n        ->{_2_}")


def get_collection_video(collection: Collection, video: Video):
    # 使用 ffmpeg 拼接视频
    video_m4s = os.path.join(video.folder, "video.m4s")
    audio_m4s = os.path.join(video.folder, "audio.m4s")
    if len(collection.videos) > 1:
        video_output = os.path.join(keep_path, f"{video.index} {video.title} {video.part}")
    else:
        video_output = os.path.join(keep_path, f"{video.title} {video.part}")

    cmd = f" {ffmpeg_path} " \
          f" -i {video_m4s} -i {audio_m4s} " \
          f" -c:v copy " \
          f" -strict experimental " \
          f" \"{video_output}.mp4\" "
    logging.info(cmd)
    os.system(cmd)


def test():
    collections = init_collections()
    for collection in collections:
        init_collection_videos(collection)
        for video in collection.videos:
            move_m4s(video)
            get_collection_video(collection, video)
        print(collection)


def setup():
    collections = init_collections()
    for collection in collections:
        init_collection_videos(collection)
        for video in collection.videos:
            move_m4s(video)
            get_collection_video(collection, video)
        print(collection)


if __name__ == '__main__':
    # test()
    setup()
