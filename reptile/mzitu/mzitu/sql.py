import os
import time
import datetime
from PIL import Image
import pyodbc
import sys

try:
    from color_print import *
    from all_class import *
    from config import *
    from tool import *
except ImportError:
    from .color_print import *
    from .all_class import *
    from .config import *
    from .tool import *


# 清空数据库
def clean_image_site(con_text):
    sql_cursor = con_text.cursor()
    sql_cursor.execute("delete from Images")
    con_text.commit()
    sql_cursor.execute("delete from Folders")
    con_text.commit()
    sql_cursor.execute("delete from Favorites")
    con_text.commit()


# 文件夹信息插入数据库
def insert_folders(con_text, folder):
    insert = "insert into [Folders] ([Name],[Path],[CreateDate],[ImgNum],[TotalSize])"
    values = "values ('{0}', '{1}', '{2}', '{3}', '{4}')" \
        .format(folder.Name, folder.Path, folder.CreateDate, folder.ImgNum, folder.TotalSize)
    insert_sql = insert + '\n' + values
    sql_cursor = con_text.cursor()
    sql_cursor.execute(insert_sql)
    con_text.commit()


# 图片信息插入数据库
def insert_images(con_text, img):
    insert = "insert into [Images] ([FolderId],[FolderName],[Name],[Path],[Type],[Size],[Width],[Height],[VisitDate],[CreateDate],[ChangeDate])"
    values = "values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}', '{8}','{9}','{10}')" \
        .format(img.FolderId, img.FolderName, img.Name, img.Path, img.Type, img.Size, img.Width, img.Height,
                img.VisitDate,
                img.CreateDate, img.ChangeDate)
    insert_sql = insert + '\n' + values
    sql_cursor = con_text.cursor()
    sql_cursor.execute(insert_sql)
    con_text.commit()


# 添加虚拟模拟的路径 IIS    F:\\ > F
def add_virtical_directory(con_text):
    sql_change = "update Images set Path=REPLACE(Path,'G:\\','G\\')"
    sql_cursor = con_text.cursor()
    sql_cursor.execute(sql_change)
    con_text.commit()

    sql_change = "update Folders set Path=REPLACE(Path,'G:\\','G\\')"
    sql_cursor = con_text.cursor()
    sql_cursor.execute(sql_change)
    con_text.commit()


# 数据插入数据库 部分
def insert_sql_has_down(con_text, meizi):
    title = meizi.title
    link = meizi.link
    category = meizi.category
    date = meizi.date
    insert = "insert into [HasDown] ([Title],[Link],[Category],[ReleaseTime])"
    values = "values ('{0}', '{1}', '{2}', '{3}')".format(title, link, category, date)
    insert_sql = insert + '\n' + values
    sql_cursor = con_text.cursor()
    sql_cursor.execute(insert_sql)
    con_text.commit()


# 下载的文件夹下文件插入数据库
def insert_sql_download_file(sql_server_con_text, folder_path):
    for root, dirs, files in os.walk(folder_path):
        if len(files) == 0:
            pass
        else:
            folder = get_folder_info(root, files)
            insert_folders(sql_server_con_text, folder)
            printGreen('folder_name :  ' + folder.Name + '\n')
            cnt = 1
        for file in files:
            path = os.path.join(root, file)
            image = get_image_info(path)
            insert_images(sql_server_con_text, image)
            if cnt % 8 != 0:
                sys.stdout.write(image.Path.split("\\")[-1] + '   ')
            else:
                sys.stdout.write(image.Path.split("\\")[-1] + '   ')
                sys.stdout.write('\r\n')
            cnt += 1
        sys.stdout.write('\r\n')
    print()


# 数据插入数据库 全部
def init_sql(con_text, rootDir):
    clean_image_site()
    cnt = 0
    for root, dirs, files in os.walk(rootDir):
        if len(files) == 0:
            pass
        else:
            folder = get_folder_info(root, files)
            insert_folders(con_text, folder)
            # sys.stdout.write(folder.Name)
            printGreen('\n' + folder.Name + '\n')
            cnt = 1
        for file in files:
            path = os.path.join(root, file)
            image = get_image_info(path)
            insert_images(con_text, image)
            if cnt % 9 != 0:
                sys.stdout.write(image.Path.split("\\")[-1] + '   ')
            else:
                sys.stdout.write('\n')
            cnt += 1
        sys.stdout.write('\n')
    add_virtical_directory()


if __name__ == "__main__":
    init_sql(sql_server_con_text, keep_path)

"""
select * from Folders
select * from Images
select * from HasDown


delete from Images
delete from HasDown
delete from Folders

"""
