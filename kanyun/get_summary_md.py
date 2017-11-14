import os
import functools

try:
    from config import *
    from tool import *
except ImportError:
    from .config import *
    from .tool import *


# 每一行的信息
class MDLine:
    Level = 0
    Folder = ''
    SplitPaths = []

    def __init__(self, level, folder, splitPaths):
        self.Level = level
        self.Folder = folder
        self.SplitPaths = splitPaths


# 判断是否存在文件夹同名的 .md 文件
def is_equal(list):
    if len(list) == 1:
        return False
    item1 = list[-1]
    item2 = list[-2]
    if item1[:-3] == item2:
        return True
    else:
        return False


# 自定义比较 将较短的放到后面
# 将第一目录下的文件放在最后
def md_line_cmp(md_line_1, md_line_2):
    split_path_1 = md_line_1.SplitPaths
    split_path_2 = md_line_2.SplitPaths
    len1 = len(split_path_1)
    len2 = len(split_path_2)
    if len1 < len2:
        return 1
    elif len1 > len2:
        return -1
    else:
        return 0


# 遍历文件来获取信息
def get_summary(all_md_line, rootDir, level=1):
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

        base_path = os.path.join(rootDir, file)

        if os.path.isdir(base_path) == True:
            # E:\Desktop\NoteBook\Web\其他
            # ->
            # ['其他', '其他.md']
            split_path = (base_path + '\\' + file + '.md').split('\\')[-level - 1:]
        else:
            # E:\Desktop\NoteBook\Web\其他\Cookie.md
            # ->
            # ['其他', 'Cookie.md']
            split_path = (rootDir + '\\' + file).split('\\')[-level:]

        print(split_path)

        md_line = MDLine(level, file, split_path)
        all_md_line.append(md_line)

        # 去除与文件夹相同的 .md 文件
        if is_equal(split_path) == True:
            if os.path.isfile(base_path) == True:
                # pass
                all_md_line.pop()

        if os.path.isdir(base_path):
            get_summary(all_md_line, base_path, level + 1)


# 根据MDLine来合成实际的line
def get_lines_by_md_line(md_lines):
    lines = []
    for md_line in md_lines:
        # print(md_line.SplitPaths)
        line = ''
        line += ' ' * (md_line.Level - 1) * 4 + '* ' + '[' + md_line.Folder + ']' + '(' + '\\'.join(
            md_line.SplitPaths) + ')'
        line = line.replace('\\', '/')
        lines.append(line)
    return lines


# 保存summary.md文件
def keep_summary(folder_path, lines):
    summary_path = folder_path + '\\' + 'SUMMARY.md'
    print('create summary.md    ' + summary_path)
    with open(summary_path, 'w+', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            file.write('\n')
    file.close()


# 创建summary.md文件
def create_summary_md():
    all_note_path = get_all_note_path()
    for node_path in all_note_path:
        md_lines = []
        get_summary(md_lines, node_path)
        md_lines.sort(key=functools.cmp_to_key(md_line_cmp))
        lines = get_lines_by_md_line(md_lines)
        keep_summary(node_path, lines)

# pp.sort(key=functools.cmp_to_key(my_cmp))


if __name__ == '__main__':
    # pass
    create_summary_md()
