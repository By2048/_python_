import os

path_folders = "D:\\"
path_icons = "D:\\Icon"
desktop_ini_data = "[.ShellClassInfo]\nIconResource = D:\Icon\{}, 0"


def init():
    """ 设置Win系统中文件夹显示的图标 """

    for folder in os.listdir(path_folders):
        folder_path = os.path.join(path_folders, folder)
        for icon in os.listdir(path_icons):
            icon_path = os.path.join(path_icons, icon)

            if folder == icon.split('.')[0]:
                desktop_ini_path = os.path.join(folder_path, 'desktop.ini')

                print(f"{folder_path:>30} -> {icon_path}")

                if os.path.isfile(desktop_ini_path):
                    os.system(f"attrib -s -h {desktop_ini_path}")

                try:
                    with open(desktop_ini_path, 'w') as file:
                        file.write(desktop_ini_data.format(icon))
                except Exception as e:
                    print(f'---------- {folder_path} - {icon_path} ----------')
                    print(e)

                os.system(f"attrib +s +h {desktop_ini_path}")

                break


def clear():
    """ 清除图标缓存 - delete desktop.ini """
    for folder in os.listdir(path_folders):
        folder_path = os.path.join(path_folders, folder)
        desktop_ini_path = os.path.join(folder_path, 'desktop.ini')

        if os.path.isfile(desktop_ini_path):
            print(f"delete {desktop_ini_path}")
            os.system(f"attrib -s -h {desktop_ini_path}")
            os.remove(desktop_ini_path)


if __name__ == '__main__':
    clear()
    init()
