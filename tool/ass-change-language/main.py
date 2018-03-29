import os
import shutil
from hanziconv import HanziConv

# 需要转换的字幕文件夹的位置
sub_path= r'E:\Desktop\Subs'

# 转换后的文件夹的位置
change_sub_path = r'E:\Desktop\Subs_Change'

# 创建文件夹
def create_folder():
    if not os.path.isdir(change_sub_path):
        os.mkdir(change_sub_path)
    if not os.path.isdir(sub_path):
        os.mkdir(sub_path)

# 进行转换
def change_ass(old_file_path,new_file_path):
    old_file = open(old_file_path, mode='r', encoding='utf-8-sig')
    new_file=open(new_file_path,mode='w',encoding='utf-8-sig')

    for line in old_file.readlines():
        new_line=HanziConv.toSimplified(line)
        new_file.write(new_line)


if __name__=='__main__':
    create_folder()
    for path in os.listdir(sub_path):
        old_file_path = sub_path + '\\' + path
        new_file_path = change_sub_path + '\\' + os.path.basename(path)
        change_ass(old_file_path,new_file_path)