import hashlib
import os
import sys
from pprint import pprint

try:
    from ._rename_ import File, init_files_info, print_files_info, rename_files
except ImportError:
    from _rename_ import File, init_files_info, print_files_info, rename_files

path = "T:\\收藏\\"
images = []


def init():
    for item in os.listdir(path):
        if len(item) == 36:
            # 已经重命名为文件的MD5
            # xx_md5_xxx.jpg 长度(36)
            continue
        old = item
        file = File(folder=path, old_name=old)
        images.append(file)


def md5(item):
    hash_md5 = hashlib.md5()
    with open(item, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_name(file: File):
    name = md5(file.old_full_path)
    return f"{name}.{file._type_}"


if __name__ == '__main__':
    init()
    init_files_info(images, get_name)
    print_files_info(images)
    rename_files(images, check=False)
