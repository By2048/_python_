import datetime
import win32file
import shutil
import os
import time
import sys


def get_udisks():
    u_disks = []
    # 124 -> 0b1111100 -> 1111100 -> 0011111 -> ABCDEFG -> 0无 1有
    sign = bin(win32file.GetLogicalDrives())[2:][::-1]
    for i in range(len(sign)):
        disk = chr(ord('A') + i) + ':\\'
        if sign[i] == '1' and win32file.GetDriveType(disk) == 2:
            u_disks.append(disk)
    return u_disks


def copy_file(udisk, computer):
    list_files = os.walk(udisk)
    for root, dirs, files in list_files:
        for file in files:
            if file.endswith(('.xlsx', '.xls', '.ppt', '.pptx', '.pdf', '.png', '.jpg', '.txt', '.doc', '.docx')):
                # if file.endswith(('.jpg')):
                shutil.copyfile(os.path.join(root, file), os.path.join(computer, file))


def copy_file_tree(udisk, computer):
    cmd = 'tree ' + udisk + ' /f > ' + computer + '\\copy_file_tree.txt'
    os.system(cmd)


if __name__ == "__main__":
    keep_path = 'F:\\Backup\\udisk-copy\\'
    # while True:
    udisks = get_udisks()
    for udisk in udisks:
        computer = keep_path + datetime.datetime.now().strftime("%Y-%m-%d--%H-%M")
        if not os.path.exists(computer):
            os.makedirs(computer)
        copy_file(udisk, computer)
        copy_file_tree(udisk, computer)
        # time.sleep(10)
