import os

try:
    from config import *
except ImportError:
    from .config import *


# 获取所有的笔记路径
def get_all_note_path():
    # 所有的笔记本文件路径
    note_paths = []
    paths = os.listdir(note_book_path)
    print(paths)
    for path in paths:
        # 去除主目录上以 排除的文件夹 README.md 文件
        if path in ignore_folder or path in ignore_file:
            continue
        note_path = os.path.join(note_book_path, path)
        note_paths.append(note_path)
    return note_paths

# 判断路径中是否包含被忽略的文件夹
def is_exit_ignore_folder(base_path):
    split_paths=base_path.split('\\')
    for _path in split_paths:
        if _path in ignore_folder:
            return True
    return False

# 判断是否是由Yu_Writer软件创建的文件夹
def is_Yu_Writer_folder(path):
    split_paths = path.split('.')
    if len(split_paths) == 1:
        return False
    if split_paths[1] == 'resource':
        return True
    else:
        return False


if __name__ == '__main__':
    all_path = get_all_note_path()
    print('\n'.join(all_path))
    pass
