# coding=utf-8
import os
import functools

try:
    from config import *
    from tool import *
except ImportError:
    from .config import *
    from .tool import *

ignore_file = ['_image']

all_md_line = []

root_path = 'T:\\开发文档\\1_53IQ开发包'

print(root_path)


# 每一行的信息
class MDLine:
    level = 0
    split_path = []

    def __init__(self, level, split_path):
        self.level = level
        self.split_path = split_path

    def __str__(self):
        return str(self.level) + '\t' + str(self.split_path)


def md_sort(a, b):
    if len(a.split_path) > len(b.split_path):
        return 1
    elif len(a.split_path) < len(b.split_path):
        return -1
    elif len(a.split_path) == len(b.split_path):
        x, y = int(a.split_path[-1].split('_')[0]), int(b.split_path[-1].split('_')[0])
        if x > y:
            return 1
        if x < y:
            return -1
        elif x == y:
            return 0


# _sidebar.md

# 遍历文件来获取信息
def get_summary(all_md_line, root_path, level=1):
    for file in os.listdir(root_path):

        # 排除文件忽略的文件
        if file in ignore_file:
            continue

        base_path = os.path.join(root_path, file)

        split_path = (root_path + '\\' + file).split('\\')[-level:]
        # print(split_path)

        _level = int(split_path[-1].split('_')[0])
        if len(split_path) == 1:
            if split_path[0].endswith('.md') == False:
                _level += 100

        md_line = MDLine(_level, split_path)
        all_md_line.append(md_line)

        if os.path.isdir(base_path):
            get_summary(all_md_line, base_path, level + 1)


if __name__ == '__main__':
    # pass
    get_summary(all_md_line, root_path, level=1)
    sorted(all_md_line, key=functools.cmp_to_key(md_sort))
    for item in all_md_line:
        print(item)
