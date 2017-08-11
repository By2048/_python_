import os


def is_git_folder(path):
    split_paths=path.split('\\')
    is_git=False
    for path in split_paths:
        if path =='.git':
            return True
    return is_git

rootPath = r'F:\_Test\Program'
for root, dirs, files in os.walk(rootPath):
    for dir in dirs:
        if dir[0] in [',','_']:
            continue
        file_path = os.path.join(root, dir)
        if is_git_folder(file_path):
            continue
        print(dir)