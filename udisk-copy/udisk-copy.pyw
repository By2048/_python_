import datetime
import win32file
import shutil
import os
import time
import re
import sys

keep_path = 'G:\\Backup\\udisk-copy\\'

def get_udisk_path():
    udisks = []
    # 124 -> 0b1111100 -> 1111100 -> 0011111 -> ABCDEFG -> 0无 1有
    sign = bin(win32file.GetLogicalDrives())[2:][::-1]
    for i in range(len(sign)):
        disk = chr(ord('A') + i) + ':\\'
        if sign[i] == '1' and win32file.GetDriveType(disk) == 2:
            udisks.append(disk)
    return udisks[0]    # 仅使用一个U盘

def get_udisk_info_by_path(path):
    all_info=os.popen("dir "+path).readlines()[0:2]
    # [' 驱动器 H 中的卷是 AM\n', ' 卷的序列号是 4A21-D15A\n']


# def create_copy_folder():



def run_cmd(cmd):
    cmd_return=os.popen(cmd)
    # info = cmd_return.read()
    info = cmd_return.readlines()[1]

    return info



#
# def get_file_path():
#
#
#
# def copy_image():
#
# def copy_document():
#
# def copy_compressed_file():
#
#
# def copy_file_tree(udisk, computer):
#     cmd = 'tree ' + udisk + ' /f > ' + computer + '\\copy_file_tree.txt'
#     os.system(cmd)
#
# def copy_other()


def copy_file(udisk, computer):
    list_files = os.walk(udisk)
    for root, dirs, files in list_files:
        for file in files: # .rar .zip .gif .bmp
            if file.endswith(('.xlsx', '.xls', '.ppt', '.pptx', '.pdf', '.png', '.jpg', '.txt', '.doc', '.docx')):
                # if file.endswith(('.jpg')):
                shutil.copyfile(os.path.join(root, file), os.path.join(computer, file))



if __name__ == "__main__":
    # while True:
    udisk_path = get_udisk_path()
    get_udisk_info_by_path(udisk_path)

    # for udisk in udisks:
    #     computer = keep_path + datetime.datetime.now().strftime("%Y-%m-%d--%H-%M")
    #     if not os.path.exists(computer):
    #         os.makedirs(computer)
    #     # copy_file_tree(udisk, computer)
    #     time.sleep(3)
    #     # copy_file(udisk, computer)
    #     # time.sleep(10)
