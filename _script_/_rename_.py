import os

from typing import List


class File(object):
    def __init__(self, old_name='', new_name=''):
        self.old_name = old_name
        self.new_name = new_name

    def __str__(self):
        return f"{self.old_name} \t {self.new_name}"


class Rename(object):
    def __init__(self):
        self.folder: str = ""  # 重命名文件夹目录
        self.files: List[File] = []  # 需要重命名的文件 新名字-旧名字
        self.function_need_rename = None  # 筛选需要重命名的文件
        self.function_get_name = None  # 重命名函数
        self.show_title = True  # 显示表格Title

    def __str__(self):
        return self.info()

    def info(self):
        try:
            from veryprettytable import VeryPrettyTable
        except ImportError:
            for file in self.files:
                print(file)
            return
        table = VeryPrettyTable(['old_name', 'new_name'])
        if self.show_title:
            table.title = self.folder
        table.align['old_name'] = 'l'
        table.align['new_name'] = 'l'
        for file in self.files:
            table.add_row([file.old_name, file.new_name])
        return table.get_string()

    def init(self):
        for item in os.listdir(self.folder):
            if not self.function_need_rename(item):
                continue
            file = File(old_name=item)
            file.new_name = self.function_get_name(item)
            self.files.append(file)

    def start(self, check=True):
        if check:
            print('\n确认重命名\n')
            check = input()
            if check not in ('1', 'true', 'y', True) or not check:
                return
        for file in self.files:
            old = os.path.join(self.folder, file.old_name)
            new = os.path.join(self.folder, file.new_name)
            os.rename(old, new)
