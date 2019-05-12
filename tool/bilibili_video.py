import logging
import os
import json
import shutil

from hanziconv import HanziConv

# https://pypi.org/project/hanziconv/  简繁体转换


logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)1.1s %(asctime)s.%(msecs)3d %(module)9s:%(lineno)3d] %(message)s',
    datefmt='%H:%M:%S'
)

ffmpeg_path = os.path.abspath('D:\\FFmpeg\\bin\\ffmpeg.exe')
download_path = 'F:\\Download\\bilibili'
keep_path = 'F:\\Download'

logging.info(f'ffmpeg_path      {ffmpeg_path}')
logging.info(f'download_path    {download_path}')
logging.info(f'new_path         {keep_path}\n')


# bilibili
# ├─13601266
# │  ├─1
# │  └─2
# ├─18038324
# │  └─1


class Video(object):
    def __init__(self, path, num, name):
        self.name = name
        self.path = path
        self.num = num

    def __str__(self):
        return f"{self.path}\t{self.name}"


def get_video_name(path, num):
    def change_name(name):
        change_code = [('?', ''), ('？', ''), ('| ', ''), ('*', ''), (' ', '_'), ('\\', '_'), ('/', '_')]
        change_code += [('【', '['), ('】', ']'), ('《', ''), ('》', ''), ('，', '')]
        for code in change_code:
            name = name.replace(code[0], code[1])
        name = HanziConv.toSimplified(name)
        return name

    with open(os.path.join(path, 'entry.json'), 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    if data.get('page_data', ''):
        video_name = data['title']
        if num != 1:
            video_name = f"{data['title']}_{data['page_data']['part']}"
        video_name = change_name(video_name)
        return video_name

    if data.get('ep', ''):
        index = data['ep']['index']
        index_title = data['ep']['index_title']
        video_name = data['title'] + '_' + index
        if index_title:
            video_name = data['title'] + '_' + index + '_' + index_title
        video_name = change_name(video_name)
        return video_name


def get_all_video():
    videos = []
    for video_folder in os.listdir(download_path):
        video_path = os.path.join(download_path, video_folder)
        for video_item in os.listdir(video_path):
            _num = len(os.listdir(video_path))
            _path = os.path.join(video_path, video_item)
            _name = get_video_name(_path, _num)
            video = Video(num=_num, path=_path, name=_name)
            videos.append(video)
            logging.info(video)
    return videos


def move_blv(videos):
    for video in videos:
        for root, dirs, files in os.walk(video.path):
            for file in files:
                if file.endswith('.blv'):
                    shutil.move(os.path.join(root, file), video.path)
                else:
                    pass


def blv_to_flv(videos):
    for video in videos:
        for file in os.listdir(video.path):
            if file.endswith('.blv'):
                old_name = os.path.join(video.path, file)
                new_name = old_name.replace('.blv', '.flv')
                os.rename(old_name, new_name)


def get_video_list(videos):
    # 在每个视频文件夹路径下获取 video_list.txt
    for video in videos:
        lines = []
        for file in os.listdir(video.path):
            if file.endswith('.flv'):
                lines.append(os.path.join(video.path, file))
        lines.sort(key=lambda x: int(os.path.basename(x).split('.')[0]), reverse=False)
        video_list_path = os.path.join(video.path, 'video_list.txt')
        with open(video_list_path, 'w+', encoding='utf-8') as file:
            for line in lines:
                file.write(f"file '{line}'\n")


def get_sum_video(videos):
    # 使用 ffmpeg 拼接视频
    for video in videos:
        video_list_path = os.path.join(video.path, 'video_list.txt')
        new_video_path = os.path.join(keep_path, video.name) + '.flv'
        cmd = f"{ffmpeg_path} -f concat -safe 0 -i {video_list_path} -c copy {new_video_path}"
        logging.info(cmd)
        os.system(cmd)


def test():
    videos = get_all_video()
    move_blv(videos)
    blv_to_flv(videos)
    get_video_list(videos)
    get_sum_video(videos)


def setup():
    videos = get_all_video()
    move_blv(videos)
    blv_to_flv(videos)
    get_video_list(videos)
    get_sum_video(videos)


if __name__ == '__main__':
    # test()
    setup()
