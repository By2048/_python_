import logging
import os
import json
import shutil

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)1.1s %(lineno)3d] %(message)s',
    datefmt='%H:%M:%S'
)

base_folder = "T:\\com.bilibili.app.in\\"
ffmpeg_path = "D:\\FFmpeg\\bin\\ffmpeg.exe"
download_path = "T:\\com.bilibili.app.in\\download\\"
keep_path = "T:\\"

# bilibili (download_path)
# ├─xxxxxxxx (Collection)
# │  ├─1 (video1)
# │  └─2 (video2)
# ├─xxxxxxxx
# │  └─1


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

    def __str__(self):
        result = f"{'video_index'.rjust(20)} {self.index}\n"
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
        logging.info(video)

    # if data.get('ep', ''):
    #     index = data['ep']['index']
    #     index_title = data['ep']['index_title']
    #     video_name = data['title'] + '_' + index
    #     if index_title:
    #         video_name = data['title'] + '_' + index + '_' + index_title
    #     video_name = change_name(video_name)
    #     return video_name


def move_m4s(video: Video):
    logging.info('-' * 66)
    for root, dirs, files in os.walk(video.folder):
        for file in files:
            if file.endswith(".m4s"):
                _1_ = os.path.join(root, file)
                _2_ = video.folder
                try:
                    shutil.move(os.path.join(root, file), video.folder)
                    logging.info(f"mv {_1_} \n        -> {_2_}")
                except shutil.Error:
                    logging.error(f"mv {_1_} \n        -> {_2_}")


def get_collection_video(collection: Collection, video: Video):
    # 使用 ffmpeg 拼接视频
    logging.info('-' * 66)
    video_m4s = os.path.join(video.folder, "video.m4s")
    audio_m4s = os.path.join(video.folder, "audio.m4s")

    names = {
        "1": f"{video.title}",
        "2": f"{video.part}",
        "3": f"{video.title} {video.part}",
        "4": f"{video.index} {video.title} {video.part}"
    }

    data = "#选项# \n"
    for key, value in names.items():
        data += f"\t\t[#{key}] {value}\n"
    data = data.rstrip("\n")
    logging.info(data)

    check = input(" #选择# ".rjust(13))
    if check not in names.keys():
        return

    name = names.get(check)
    if not name:
        return

    video_output = os.path.join(keep_path, name)

    logging.info('-' * 66)
    cmd = f" {ffmpeg_path} " \
          f" -i {video_m4s} -i {audio_m4s} " \
          f" -c:v copy " \
          f" -strict experimental " \
          f" \"{video_output}.mp4\" "
    logging.info(cmd)
    logging.info('-' * 66)
    os.system(cmd)


def clear():
    check = input(" #删除# ".rjust(13))
    if check in ['1', 'y']:
        shutil.rmtree(base_folder)


def test():
    pass


def setup():
    collections = init_collections()
    for collection in collections:
        init_collection_videos(collection)
        for video in collection.videos:
            move_m4s(video)
            get_collection_video(collection, video)
    clear()


if __name__ == '__main__':
    setup()
