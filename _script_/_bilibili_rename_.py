import re
import os

path = ''  # 文件夹路径
videos = []  # 视频文件名

try:
    from ._rename_ import File, init_files_info, print_files_info, rename_files
except ImportError:
    from _rename_ import File, init_files_info, print_files_info, rename_files


def init():
    print("\n粘贴文件夹路径\n")
    global path
    path = input()
    path = path.strip('"')

    if os.path.isfile(path):
        file = File()
        file.folder = os.path.dirname(path)
        file.old_name = os.path.basename(path)
        videos.append(file)

    for item in os.listdir(path):
        file = File(folder=path, old_name=item)
        videos.append(file)


def get_name(file: File):
    item = file.old_name.split('.')
    try:
        index, name, file_type = item[0].zfill(2), item[1], item[2]
    except Exception as e:
        print(f'\n文件名解析错误 {file.old_name}\n')
        return False
    video_title = ''.join(re.split(r'\([avAVpP,\d]+\)', name))  # 去除(Avxxxxxx,Pxxxxx)
    new_name = f"{index} {video_title}.{file_type}"
    return new_name


if __name__ == '__main__':
    init()
    init_files_info(videos, get_name)
    print_files_info(videos)
    rename_files(videos)
