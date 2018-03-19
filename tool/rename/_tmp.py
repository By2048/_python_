import os

_path = 'H:\\one piece\\one piece'


def Test1(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for file in files:
            old_name = os.path.join(root, file)
            if old_name.endswith('.jpg'):
                pass
            else:
                new_file_name = file.replace('.mhr', '.jpg')[1:]
                new_name = os.path.join(root, new_file_name)
                print(old_name + '\t-->\t' + new_name)
                os.rename(old_name, new_name)


Test1(_path)
