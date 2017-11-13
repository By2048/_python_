import os
import functools

try:
    from config import *
    from tool import *
except ImportError:
    from .config import *
    from .tool import *


class MDLine:
    Level = 0
    Folder = ''
    SplitPaths = []

    def __init__(self, level, folder, splitPaths):
        self.Level = level
        self.Folder = folder
        self.SplitPaths = splitPaths


# 将子目录拼接
def my_join(lists):
    path = ''
    for list in lists[:-1]:
        path += list + '\\'
    path += lists[len(lists) - 1]
    return path


def is_equal(list):
    if len(list) == 1:
        return False
    item1 = list[-1]
    item2 = list[-2]
    if item1[:-3] == item2:
        return True
    else:
        return False


def get_summary(md_lines, rootDir, level=1):
    for file in os.listdir(rootDir):
        # 排除文件忽略的文件
        if file in ignore_file:
            continue
        # 排除完整文件路径中含有忽略的文件夹
        if is_exit_ignore_folder(os.path.join(rootDir, file)):
            continue
        # 忽略Yu_writee文件夹
        if is_Yu_Writer_folder(os.path.join(rootDir, file)):
            continue

        path = os.path.join(rootDir, file)

        if os.path.isdir(path) == True:
            split_path = (path + '\\' + file + '.md').split('\\')[-level - 1:]
        else:
            split_path = (rootDir + '\\' + file).split('\\')[-level:]


        md_line = MDLine(level, file, split_path)
        md_lines.append(md_line)

        # 去除与文件夹相同的 .md 文件
        if is_equal(split_path) == True:
            if os.path.isfile(path) == True:
                # pass
                md_lines.pop()

        if os.path.isdir(path):
            get_summary(md_lines, path, level + 1)
    return md_lines


def get_lines_by_md_line(md_lines):
    lines = []
    for md_line in md_lines:
        # print(md_line.SplitPaths)
        line = ''
        line += ' ' * (md_line.Level - 1) * 4 + '* ' + '[' + md_line.Folder + ']' + '(' + my_join(
            md_line.SplitPaths) + ')'
        line = line.replace('\\', '/')
        lines.append(line)
    return lines


def keep_summary(folder_path, lines):
    summary_path = folder_path + '\\' + 'SUMMARY.md'
    print('create summary.md    ' + summary_path)
    with open(summary_path, 'w+', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            file.write('\n')
    file.close()


def create_summary_md():
    note_paths = get_all_note_path()
    for node_path in note_paths:
        md_lines = []
        md_lines = get_summary(md_lines, node_path)
        lines = get_lines_by_md_line(md_lines)
        keep_summary(node_path, lines)


if __name__ == '__main__':
    # pass
    create_summary_md()
