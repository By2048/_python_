# -*- coding: utf-8 -*-
import os
import time
import datetime
from PIL import Image
import pyodbc
import sys

try:
    from color_print import *
except ImportError:
    from .color_print import *

con_text = pyodbc.connect('DRIVER={SQL Server};SERVER=.;DATABASE=ImageSite;UID=Link-ImageSite;PWD=P@ssw0rd')


# 清空数据库
def clean_image_site():
    sql_cursor = con_text.cursor()
    sql_cursor.execute("delete from Images")
    con_text.commit()
    sql_cursor.execute("delete from Folders")
    con_text.commit()


# 文件夹信息
class Folder:
    Name = ""
    Path = ""
    CreateDate = ""  # 文件夹创建时间
    ImgNum = ""
    TotalSize = ""

    def __init__(self, name, path, createDate, imgNum, totalSize):
        self.Name = name
        self.Path = path
        self.CreateDate = createDate
        self.ImgNum = imgNum
        self.TotalSize = totalSize


# 图片信息(Img)
class Img:
    FolderId = ""
    Name = ""
    Path = ""
    Type = ""
    Size = ""  # 图片大小
    Width = ""
    Height = ""
    VisitDate = ""  # 文件最后访问时间
    CreateDate = ""  # 文件创建时间
    ChangeDate = ""  # 文件最后修改时间

    def __init__(self, folderId, name, path, type, size, width, heigth, visitDate, createDate, changeDate):
        self.FolderId = folderId
        self.Name = name
        self.Path = path
        self.Type = type
        self.Size = size
        self.Width = width
        self.Height = heigth
        self.VisitDate = visitDate
        self.CreateDate = createDate
        self.ChangeDate = changeDate


# 获取图片文件的信息  文件夹名 路径 创建时间 文件夹内图片数量 文件的大小
def get_folder_info(root, files):
    create_date = datetime.datetime.fromtimestamp(os.path.getctime(root)).strftime('%Y-%m-%d %H:%M:%S')
    name = root.split('\\')[-1]
    path = root
    img_num = len(files)
    _size = sum([os.path.getsize(os.path.join(root, name)) for name in files]) / 1024 / 1024
    total_size = round(_size, 2)
    return Folder(name, path, create_date, img_num, total_size)


# 获取图片文件具体信息
def get_images(path):
    name = os.path.basename(path)
    folder_name = os.path.splitext(path)[0].split('\\')[-2]
    folder_id = get_folder_id(folder_name)
    type = os.path.splitext(path)[1].replace(".", "")
    size = int(os.path.getsize(path) / 1024)
    atime = os.path.getatime(path)  # 文件最后访问时间
    ctime = os.path.getctime(path)  # 文件创建时间
    mtime = os.path.getmtime(path)  # 文件最后修改时间
    _atime = time.localtime(atime)
    _ctime = time.localtime(ctime)
    _mtime = time.localtime(mtime)
    visit_date = str(_atime[0]) + "-" + str(_atime[1]) + "-" + str(_atime[2]) + " " + \
                 str(_atime[3]) + ":" + str(_atime[4]) + ":" + str(_atime[5])
    create_date = str(_ctime[0]) + "-" + str(_ctime[1]) + "-" + str(_ctime[2]) + " " + \
                  str(_ctime[3]) + ":" + str(_ctime[4]) + ":" + str(_ctime[5])
    change_date = str(_mtime[0]) + "-" + str(_mtime[1]) + "-" + str(_mtime[2]) + " " + \
                  str(_mtime[3]) + ":" + str(_mtime[4]) + ":" + str(_mtime[5])
    width = Image.open(path).size[0]
    height = Image.open(path).size[1]
    return Img(folder_id, name, path, type, size, width, height, visit_date, create_date, change_date)


# 文件夹信息插入数据库
def insert_folders(folder):
    insert = "insert into [Folders] ([Name],[Path],[CreateDate],[ImgNum],[TotalSize])"
    values = "values ('{0}', '{1}', '{2}', '{3}', '{4}')" \
        .format(folder.Name, folder.Path, folder.CreateDate, folder.ImgNum, folder.TotalSize)
    insert_sql = insert + '\n' + values
    sql_cursor = con_text.cursor()
    sql_cursor.execute(insert_sql)
    con_text.commit()


# 图片信息插入数据库
def insert_images(img):
    insert = "insert into [Images] ([FolderId],[Name],[Path],[Type],[Size],[Width],[Height],[VisitDate],[CreateDate],[ChangeDate])"
    values = "values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}','{9}')" \
        .format(img.FolderId, img.Name, img.Path, img.Type, img.Size, img.Width, img.Height, img.VisitDate,
                img.CreateDate, img.ChangeDate)
    insert_sql = insert + '\n' + values
    sql_cursor = con_text.cursor()
    sql_cursor.execute(insert_sql)
    con_text.commit()


# 添加虚拟模拟的历经 IIS    F:\\ > F
def add_virtical_directory():
    sql_change = "update Images set Path=REPLACE(Path,'F:\\','F')"
    sql_cursor = con_text.cursor()
    sql_cursor.execute(sql_change)
    con_text.commit()


# Folders中的FolderId == Images的FolderId  先插入文件夹信息再插入图片信息
def get_folder_id(folder_name):
    try:
        sql_cursor = con_text.cursor()
        search_sql = "select Id from Folders where Name='{0}'".format(folder_name)
        sql_cursor.execute(search_sql)
        row = sql_cursor.fetchone()
    except:
        return '0'
    return str(row.Id)


# 输出文件夹信息
def folder_print(folder):
    print(folder.Name)
    print(folder.Path)
    print(folder.CreateDate)
    print(folder.ImgNum)
    print(folder.TotalSize)
    print('\n')


# 输出图片信息
def image_print(img):
    print(img.FolderId)
    print(img.Name)
    print(img.Path)
    print(img.Type)
    print(img.Size)
    print(img.Width)
    print(img.Height)
    print(img.VisitDate)
    print(img.CreateDate)
    print(img.ChangeDate)
    print('\n')


# 数据插入数据库 部分 -- Test
def insert_sql(folder_path):
    for root, dirs, files in os.walk(folder_path):
        if len(files) == 0:
            pass
        else:
            folder = get_folder_info(root, files)
            insert_folders(folder)
            # sys.stdout.write(folder.Name)
            printGreen('folder_name :  ' + folder.Name + '\n')
            cnt = 1
        for file in files:
            path = os.path.join(root, file)
            image = get_images(path)
            insert_images(image)
            if cnt % 8 != 0:
                sys.stdout.write(image.Path.split("\\")[-1] + '   ')
            else:
                sys.stdout.write(image.Path.split("\\")[-1] + '   ')
                sys.stdout.write('\r\n')
            cnt += 1
        sys.stdout.write('\r\n')
    add_virtical_directory()


# 数据插入数据库 全部
def init_sql():
    clean_image_site()
    rootDir = "F:\\Image\\mzitu"
    for root, dirs, files in os.walk(rootDir):
        if len(files) == 0:
            pass
        else:
            folder = get_folder_info(root, files)
            insert_folders(folder)
            # sys.stdout.write(folder.Name)
            printGreen('\n' + folder.Name + '\n')
            cnt = 1
        for file in files:
            path = os.path.join(root, file)
            image = get_images(path)
            insert_images(image)
            if cnt % 9 != 0:
                sys.stdout.write(image.Path.split("\\")[-1] + '   ')
            else:
                sys.stdout.write('\n')
            cnt += 1
        sys.stdout.write('\n')
    add_virtical_directory()


if __name__ == "__main__":
    init_sql()
    # fpath="F:\\Image\\mzitu\\抚媚熟女的黑丝诱惑 Beautyleg美腿写真 No2068 Vicni"
    # insert_sql(fpath)
