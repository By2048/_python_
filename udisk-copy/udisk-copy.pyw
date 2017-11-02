import datetime
import win32file
import shutil
import os
import time
import re
import sys

keep_path = 'G:\\Backup\\udisk-copy\\'

def get_all_udisk_path():
    udisks = []
    # 124 -> 0b1111100 -> 1111100 -> 0011111 -> ABCDEFG -> 0无 1有
    sign = bin(win32file.GetLogicalDrives())[2:][::-1]
    for i in range(len(sign)):
        disk = chr(ord('A') + i) + ':\\'
        if sign[i] == '1' and win32file.GetDriveType(disk) == 2:
            udisks.append(disk)
    return udisks

# [' 驱动器 H 中的卷是 AM\n', ' 卷的序列号是 4A21-D15A\n']
def get_udisk_info_by_path(path):
    info=os.popen("dir "+path).readlines()[0:2]
    return info



def run_cmd(cmd):
    cmd_return=os.popen(cmd)
    # info = cmd_return.read()
    info = cmd_return.readlines()[1]
    return info



# def get_file_path():
#
#
#
# def copy_image():
#
# def copy_document():
#
# def copy_compressed_file():


def get_folder_name(udisk_path):
    info=get_udisk_info_by_path(udisk_path)
    info="".join(info)
    info = info.replace('\n', '')
    match = re.search(r'(\S{4})(-)(\S{4})', info)
    name=match.group()
    return name

def copy_file_tree(udisk_path):
    name=get_folder_name(udisk_path)
    cmd = 'tree ' + udisk_path + ' /f > ' + keep_path + name+'.txt'
    os.system(cmd)


def create_folder(path):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)

def copy_file(old_path,new_path):
    if os.path.exists(new_path):
        pass
    else:
        shutil.copyfile(old_path, new_path)


def copy_file(udisk_path,folder_path):
    copy_list=['.xlsx', '.xls', '.ppt', '.pptx', '.pdf', '.png', '.jpg', '.txt', '.doc', '.docx','.gif','.bmp']
    # .rar .zip
    for root, dirs, files in os.walk(udisk_path):
        for file in files:
            if os.path.splitext(file)[1] in copy_list:
                # pass
                old_path=os.path.join(root,file)
                new_path=folder_path+old_path[2:]
                folder_name=os.path.dirname(new_path)
                create_folder(folder_name)
                print(old_path+'\n'+new_path+'\n')

                copy_file(old_path, new_path)


if __name__ == "__main__":
    all_udisk_path = get_all_udisk_path()
    # ['X:\\', 'Y:\\', 'Z:\\']

    for udisk_path in all_udisk_path:
        folder_name=get_folder_name(udisk_path)

        folder_path = keep_path + folder_name
        create_folder(folder_path)

        copy_file(udisk_path, folder_path)
