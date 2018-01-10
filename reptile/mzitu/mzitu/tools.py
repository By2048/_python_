import os
import time
import datetime
from PIL import Image as PILImage
import pyodbc
import sys
import re

try:
    from .config import *
    from .items import *
    from .sql import *
except ImportError:
    from items import *
    from config import *
    from sql import *


# 编码转换 仅去除系统不允许的字符
def change_coding(in_str):
    # Win系统不允许的文件名 \ / : * ? ' < > |
    # 操作系统限制 使用特殊标记替换字符 方便后期恢复
    # question_mark(?)
    # colon_mark(:)
    in_str = in_str.replace('？', '(qm)') \
        .replace('?', '(qm)') \
        .replace(':', '(cm)')

    out_str = ''
    remove_code = ['\\', '/', '*', '\'', '<', ' > ', '|', ]
    for item in in_str:
        if item in remove_code:
            out_str += ' '
        else:
            out_str += item
    # 去除末尾可能存在的空格
    out_str = out_str.strip()
    return out_str


# 获取图片文件的信息  文件夹名 路径 创建时间 文件夹内图片数量 文件的大小
def get_folder_info(root, files):
    create_date = datetime.datetime.fromtimestamp(os.path.getctime(root)).strftime('%Y-%m-%d %H:%M:%S')
    name = root.split('\\')[-1]
    path = root
    img_num = len(files)
    _size = sum([os.path.getsize(os.path.join(root, name)) for name in files]) / 1024 / 1024
    total_size = round(_size, 2)
    return MFolder(name, path, create_date, img_num, total_size)


# Folders中的FolderId == Images的FolderId  先插入文件夹信息再插入图片信息
def get_folder_id(con_text, folder_name):
    try:
        sql_cursor = con_text.cursor()
        search_sql = "select Id from Folders where Name='{0}'".format(folder_name)
        sql_cursor.execute(search_sql)
        row = sql_cursor.fetchone()
    except:
        return '0'
    return str(row.Id)


# 获取图片文件具体信息
def get_image_info(path):
    name = os.path.basename(path)
    folder_name = os.path.splitext(path)[0].split('\\')[-2]
    folder_id = get_folder_id(sql_server_con_text, folder_name)
    type = os.path.splitext(path)[1].replace('.', '')
    size = int(os.path.getsize(path) / 1024)
    atime = os.path.getatime(path)  # 文件最后访问时间
    ctime = os.path.getctime(path)  # 文件创建时间
    mtime = os.path.getmtime(path)  # 文件最后修改时间
    _atime = time.localtime(atime)
    _ctime = time.localtime(ctime)
    _mtime = time.localtime(mtime)
    visit_date = str(_atime[0]) + '-' + str(_atime[1]) + '-' + str(_atime[2]) + ' ' + \
                 str(_atime[3]) + ':' + str(_atime[4]) + ':' + str(_atime[5])
    create_date = str(_ctime[0]) + '-' + str(_ctime[1]) + '-' + str(_ctime[2]) + ' ' + \
                  str(_ctime[3]) + ':' + str(_ctime[4]) + ':' + str(_ctime[5])
    change_date = str(_mtime[0]) + '-' + str(_mtime[1]) + '-' + str(_mtime[2]) + ' ' + \
                  str(_mtime[3]) + ':' + str(_mtime[4]) + ':' + str(_mtime[5])
    width, height = PILImage.open(path).size[0], PILImage.open(path).size[1]
    return MImage(folder_id, folder_name, name, path, type, size, width, height, visit_date, create_date,
                  change_date)
