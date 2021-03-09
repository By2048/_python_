import os
import shutil

import win32file

free_bytes, total_bytes, total_free_bytes = win32file.GetDiskFreeSpaceEx('e:\\')
print(free_bytes / 1024 / 1024 / 1024)
print(total_bytes / 1024 / 1024 / 1024)
print(total_free_bytes / 1024 / 1024 / 1024)

# 3.4221725463867188
# 6.768466949462891
# 3.4221725463867188

# 124 （十进制） -> 0b1111100 （二进制） -> 1111100 -> 0011111（逆序）
# 整数对应于可用的驱动器：每个可用驱动器获得1位。所以如果没有驱动器可用，你会得到0
sign = bin(win32file.GetLogicalDrives())[2:][::-1]

# 获取驱动器的类型
win32file.GetDriveType(disk)


# |   DRIVE_UNKNOWN 0            |   不能确定驱动器类型。
# |   DRIVE_NO_ROOT_DIR 1        |    根路径无效; 例如，没有卷安装在指定的路径。
# |   DRIVE_REMOVABLE 2          |    驱动器具有可移动介质; 例如软盘驱动器，拇指驱动器或闪存卡读取器。
# |   DRIVE_FIXED 3              |    驱动器具有固定介质; 例如，硬盘驱动器或闪存驱动器。
# |   DRIVE_REMOTE 4             |    驱动器是远程（网络）驱动器。
# |   DRIVE_CDROM 5              |    驱动器是CD-ROM驱动器。
# |   DRIVE_RAMDISK 6            |     驱动器是RAM磁盘。


# 参考连接
# https://msdn.microsoft.com/en-us/library/windows/desktop/aa364939(v=vs.85).aspx
# http://stackoverflow.com/questions/33790734/python-getlogicaldrives-bitwise-and


def get_udisks():
    u_disks = []
    # 124 -> 0b1111100 -> 1111100 -> 0011111
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
            # if file.endswith(('.xlsx', '.xls', '.ppt', '.pptx', '.pdf', '.jpg', '.txt', '.doc', '.docx')):
            if file.endswith(('.jpg')):
                print(os.path.join(root, file))
                shutil.copyfile(os.path.join(root, file), os.path.join(computer, file))


if __name__ == "__main__":
    computer = 'f:\\Test'
    udisks = get_udisks()
    for udisk in udisks:
        copy_file(udisk, computer)
