import os
import functools

try:
    from get_empty_folder_md import is_Yu_Writer_folder
except ImportError:
    from .get_empty_folder_md import is_Yu_Writer_folder


class MDLine:
    Level = 0
    Folder = ''
    SplitPaths = []
    def __init__(self, level, folder, splitPaths):
        self.Level = level
        self.Folder = folder
        self.SplitPaths = splitPaths


def my_join(lists):
    path = ''
    for list in lists[:-1]:
        path += list + '\\'
    path += lists[len(lists) - 1]
    return path


def is_exit_md(list):
    item = list[len(list) - 1]
    print(str(item[-2:]))
    if str(item[-2:]) == 'md':
        return True
    else:
        return False


def is_equal(list):
    if len(list) == 1:
        return False
    item1 = list[-1]
    item2 = list[-2]
    if item1[:-3] == item2:
        return True
    else:
        return False


def exit__code_path(path):
    for item in path.split('\\'):
        if item == '_code':
            print('===>   ' + path)
            return True
    return False


# or is_code_folder(os.path.abspath(folder)) == True \


# 设置忽略的 文件夹 文件 信息
def is_ignore(folder):
    if folder.endswith(('.json', '.pdf', '.mhtml')) \
            or folder.startswith(('_', '.')) \
            or folder == 'SUMMARY.md' \
            or folder == 'HtmlKeep' \
            or is_Yu_Writer_folder(folder) == True:
        return True
    else:
        return False


md_lines = []
lines = []


def get_summary(rootDir, level=1):
    # if level == 1:
    #     print(rootDir)
    for folder in os.listdir(rootDir):
        # if exit__code_path(os.path.abspath(folder)) == True :
            # continue
        if is_ignore(folder):
            continue

        path = os.path.join(rootDir, folder)
        # print('----> '+path)
        # if exit__code_path(path) == True :
        #     continue
        if os.path.isdir(path) == True:
            split_path = (path + '\\' + folder + '.md').split('\\')[-level - 1:]
        else:
            split_path = (rootDir + '\\' + folder).split('\\')[-level:]

        # print(split_path)

        md_line = MDLine(level, folder, split_path)
        md_lines.append(md_line)

        # line=''
        # line+=' '* (level - 1)*4+'* '+'['+folder+']'+'('+my_join(split_path)+')'
        # line=line.replace('\\','/')
        # lines.append(line)

        if is_equal(split_path) == True:
            if os.path.isfile(path) == True:
                # lines.pop()
                md_lines.pop()

        if os.path.isdir(path):
            get_summary(path, level + 1)

    return lines


def get_lines_by_md_line():
    for md_line in md_lines:
        # print(md_line.SplitPaths)
        line = ''
        line += ' ' * (md_line.Level - 1) * 4 + '* ' + '[' + md_line.Folder + ']' + '(' + my_join(
            md_line.SplitPaths) + ')'
        line = line.replace('\\', '/')
        lines.append(line)


def keep_summary(start_path):
    summary_path = start_path + '\\' + 'SUMMARY.md'
    print('create summary.md    ' + summary_path)
    with open(summary_path, 'w+', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            file.write('\n')
    file.close()
    clean()



def clean():
    md_lines.clear()
    lines.clear()


def create_summary_md(path):
    get_summary(path)
    get_lines_by_md_line()
    keep_summary(path)


if __name__ == '__main__':
    # Test...
    pass
