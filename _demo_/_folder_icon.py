import os


def init():
    pass


def replace():
    """ 替换Win系统中文件夹显示的图标 """
    path = "d:\\"

    for folder in os.listdir(path):
        folder = os.path.join(path, folder)
        desktop = os.path.join(folder, 'desktop.ini')
        if os.path.isfile(desktop):
            with open(desktop) as file:
                data = file.read()
                data = data.replace(r'E:\Sync\Software\Icon', r'D:\Icon')

                print(desktop)

                command = f"attrib -s -h {desktop}"
                os.system(command)

                try:
                    with open(desktop, 'w') as _file_:
                        _file_.write(data)
                except Exception as e:
                    print('----------    ', desktop, '    ----------')
                    print(e)

                command = f"attrib +s +h {desktop}"
                os.system(command)


if __name__ == '__main__':
    pass
