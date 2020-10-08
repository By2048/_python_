import os

from typing import List


class File(object):
    def __init__(self, folder='', old_name='', new_name=''):
        self.folder = folder
        self.old_name = old_name
        self.new_name = new_name

    @property
    def _name_(self):
        return os.path.splitext(self.old_name)[0]

    @property
    def _type_(self):
        return os.path.splitext(self.old_name)[-1].lstrip(".")

    @property
    def old_full_path(self):
        return os.path.join(self.folder, self.old_name)

    @property
    def new_full_path(self):
        return os.path.join(self.folder, self.new_name)

    def __str__(self):
        return f"{self.old_name} \t {self.new_name}"


def init_files_info(files: List[File], function):
    for file in files:
        file.new_name = function(file)


def print_files_info(files: List[File]):
    try:
        from veryprettytable import VeryPrettyTable
    except ImportError:
        for file in files:
            print(file)
        return
    table = VeryPrettyTable(['old_name', 'new_name'])
    table.align['old_name'] = 'l'
    table.align['new_name'] = 'l'
    for file in files:
        table.add_row([file.old_name, file.new_name])
    print(table)


def rename_files(files: List[File], check=True):
    #
    if check:
        print('\n确认重命名\n')
        check = input()
        if check not in ('1', 'true', 'y', True) or not check:
            return

    for file in files:
        if not file.old_name or not file.new_name:
            print(f'获取文件名错误\n{file}')
            return

    for file in files:
        old = os.path.join(file.folder, file.old_name)
        new = os.path.join(file.folder, file.new_name)
        os.rename(old, new)
