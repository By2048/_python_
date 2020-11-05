import os
import hashlib

path_folders = "D:\\"
path_icons = "D:\\Icon"
desktop_ini_data = """
[.ShellClassInfo]
IconResource={},0
"""
desktop_ini_data = desktop_ini_data.strip('\n')


def init():
    """ 设置Windows系统中文件夹显示的图标 """
    for folder in os.listdir(path_folders):
        folder_path = os.path.join(path_folders, folder)
        if not os.path.isdir(folder_path):
            continue

        hash_icon = hashlib.md5(folder.encode("utf-8")).hexdigest()[:6]
        hash_icon_path = f"{path_icons}\\#hash-{hash_icon}.ico"
        name_icon_path = f"{path_icons}\\{folder}.ico"

        icon_file_path = ""
        if os.path.exists(hash_icon_path):
            icon_file_path = hash_icon_path
        if os.path.exists(name_icon_path):
            icon_file_path = name_icon_path

        if not icon_file_path:
            continue

        desktop_ini_path = os.path.join(folder_path, 'desktop.ini')

        print(f"{folder_path:>30} -> {icon_file_path}")

        if os.path.isfile(desktop_ini_path):
            os.system(f" attrib -s -h \"{desktop_ini_path}\" ")

        try:
            with open(desktop_ini_path, 'w', encoding="utf-8") as file:
                file.write(desktop_ini_data.format(icon_file_path))
        except Exception as e:
            print(f'---------- {folder_path} - {icon_file_path} ----------')
            print(e)

        os.system(f" attrib +h +s \"{desktop_ini_path}\" ")
        os.system(f" attrib +r \"{folder_path}\" ")


def clear():
    """ 清除图标缓存 - del desktop.ini """
    for folder in os.listdir(path_folders):
        folder_path = os.path.join(path_folders, folder)
        desktop_ini_path = os.path.join(folder_path, 'desktop.ini')
        if not os.path.isfile(desktop_ini_path):
            continue
        print(f" delete \"{desktop_ini_path}\" ")
        os.system(f" attrib -s -h \"{desktop_ini_path}\" ")
        os.remove(desktop_ini_path)


if __name__ == '__main__':
    clear()
    init()
