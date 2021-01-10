import re
import os

try:
    from ._rename_ import Rename
except ImportError:
    from _rename_ import Rename


def need_rename(item):
    return bool(item)


def get_name(item):
    item = item.split('.')
    try:
        index, name, file_type = item[0].zfill(2), item[1], item[2]
    except Exception as e:
        print(f'\n文件名解析错误 {item}\n')
        return False
    video_title = ''.join(re.split(r'\([avAVpP,\d]+\)', name))  # 去除(Avxxxxxx,Pxxxxx)
    new_name = f"{index} {video_title}.{file_type}"
    return new_name


if __name__ == '__main__':
    print("\n粘贴文件夹路径\n")
    path = input()
    path = path.strip('"')

    rename = Rename()
    rename.folder = path
    rename.function_need_rename = need_rename
    rename.function_get_name = get_name
    rename.init()
    print(rename)
    rename.start()
