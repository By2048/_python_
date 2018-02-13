import os, json, shutil
from hanziconv import HanziConv

# download
# ├─13601266
# │  ├─1
# │  └─2
# ├─18038324
# │  └─1
# ├─18620260
# │  └─1
# └─19051909
#     └─1
download_path = 'T:\\download'
new_path = 'T:\\tmp'
ffmpeg_path = os.path.abspath('..\\lib\\ffmpeg.exe')

all_bvideo = []


class BVideo():
    def __init__(self, path, num, name):
        self.path = path
        self.num = num
        self.name = name

    def show(self):
        print(self.path, end='\t')
        print(self.num, end='\t')
        print(self.name, end='\t')
        print()


def get_video_name(_path, _num):
    json_path = os.path.join(_path, 'entry.json')
    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        title = json_data['title']
        try:
            if json_data['page_data'] != None:
                if _num == 1:
                    page_data = ''
                else:
                    page_data = '_' + json_data['page_data']['part']
                video_name = title + page_data
                video_name=change_name(video_name)
                return video_name
        except KeyError:
            if json_data['ep'] != None:
                if _num == 1:
                    index = json_data['ep']['index']
                    index_title = json_data['ep']['index_title']
                    if index_title == "":
                        video_name = title + '_' + index
                    else:
                        video_name = title + '_' + index + '_' + index_title
                else:
                    index = json_data['ep']['index']
                    index_title = json_data['ep']['index_title']
                    if index_title == "":
                        video_name = title + '_' + index
                    else:
                        video_name = title + '_' + index + '_' + index_title
            video_name=change_name(video_name)
            return video_name


def get_all_bvideo():
    for av_folder in os.listdir(download_path):
        av_path = os.path.join(download_path, av_folder)
        for page_fodler in os.listdir(av_path):
            _num = len(os.listdir(av_path))
            _path = os.path.join(av_path, page_fodler)
            _name = get_video_name(_path, _num)
            bvideo = BVideo(num=_num, path=_path, name=_name)
            all_bvideo.append(bvideo)
            bvideo.show()


def move_blv():
    for video in all_bvideo:
        for root, dirs, files in os.walk(video.path):
            for file in files:
                if file.endswith('.blv'):
                    shutil.move(os.path.join(root, file), video.path)
                else:
                    pass


def blv_to_flv():
    for video in all_bvideo:
        for file in os.listdir(video.path):
            if file.endswith('.blv'):
                old_name = os.path.join(video.path, file)
                new_name = old_name.replace('.blv', '.flv')
                os.rename(old_name, new_name)
            else:
                pass


# 在每个视频文件夹路径下获取 video_list.txt
def get_video_list():
    file_line = []
    for video in all_bvideo:
        for file in os.listdir(video.path):
            if file.endswith(('.flv')):
                file_line.append(os.path.join(video.path, file))
        file_line.sort(key=lambda x: int(os.path.basename(x).split('.')[0]), reverse=False)
        video_list_path = os.path.join(video.path, 'video_list.txt')
        with open(video_list_path, 'w+', encoding='utf-8') as file:
            for line in file_line:
                file.write('file' + ' ' + '\'' + line + '\'')
                file.write('\n')


# 使用 ffmpeg 拼接视频
def get_sum_video():
    for video in all_bvideo:
        video_list_path = os.path.join(video.path, 'video_list.txt')
        new_video_path = os.path.join(new_path, video.name) + '.flv'
        cmd = "{0} -f concat -safe 0 -i {1} -c copy {2}".format(ffmpeg_path, video_list_path, new_video_path)
        print(cmd + '\n')
        os.system(cmd)


def change_name(old_name):
    new_name = old_name \
        .replace('?', '') \
        .replace('？', '') \
        .replace('| ', '') \
        .replace('*', '')\
        .replace(' ','_')
# .replace('【', '[') \
# .replace('】', ']')
# .replace('《','')\
# .replace('》','')\
# .replace('，','')\
    new_name = HanziConv.toSimplified(new_name)
    return new_name

def _test():
    _path = '..\\lib\\ffmpeg.exe'
    print(os.path.abspath(_path))
    print(os.getcwd())


if __name__ == '__main__':
    get_all_bvideo()
    move_blv()
    blv_to_flv()
    get_video_list()
    get_sum_video()

    # _test()
