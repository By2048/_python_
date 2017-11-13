import os

try:
    from config import *
    from tool import *
except ImportError:
    from .config import *
    from .tool import *

all_note_path = get_all_note_path()


# 创建空文件夹的同名的 .md 文件
def create_empty_folder_md():
    for root, folders, files in os.walk(note_book_path):
        for folder in folders:
            file_path = os.path.join(root, folder)

            # 一级目录忽略
            if file_path in all_note_path:
                continue
            # 忽略ignore文件夹
            if is_exit_ignore_folder(file_path):
                continue
            # 忽略Yu_writee文件夹
            if is_Yu_Writer_folder(file_path) == True:
                continue

            # 文件夹下所有的文件
            all_file = os.listdir(os.path.join(root, folder))
            # 存在 文件名.md pass
            if (folder + '.md') in all_file:  # exit .md
                pass
            else:
                # 创建 文件夹.md
                new_empty_folder_path = os.path.join(root, folder) + '\\' + folder + '.md'
                print('create [folder].md    ' + new_empty_folder_path)
                new_file = open(new_empty_folder_path, 'w')
                new_file.close()


if __name__ == '__main__':
    create_empty_folder_md()
    pass
