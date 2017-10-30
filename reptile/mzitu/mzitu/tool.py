import os
import time
import datetime
from PIL import Image
import pyodbc
import sys


try:
    from all_class import *
    from config import *
    from sql import *
except ImportError:
    from .config import *
    from .all_class import *
    from .sql import *


# 编码转换 去除非 汉字 英文字符
def change_coding(inStr):
    outStr = ""
    is_zh = re.compile(r"[\u4e00-\u9fff]")
    is_en = re.compile(r"[A-Za-z]")
    is_num = re.compile(r"[0-9]")
    is_spaces = re.compile(r"[\s]+")
    is_point = re.compile(r".")
    is_backslash = re.compile(r"\\")
    is_question_mark = re.compile(r"\?")
    is_exclamation_point = re.compile(r"! ")
    try:
        for word in inStr:
            if re.match(is_zh, word) != None:
                outStr += re.match(is_zh, word).group()
            elif re.match(is_en, word) != None:
                outStr += re.match(is_en, word).group()
            elif re.match(is_num, word) != None:
                outStr += re.match(is_num, word).group()
            elif re.match(is_spaces, word) != None:
                outStr += " "
            elif re.match(is_backslash, word) != None:
                outStr += ""
            elif re.match(is_point, word) != None:
                outStr += ""
            elif re.match(is_question_mark, word) != None:
                outStr += ""
            elif re.match(is_exclamation_point, word) != None:
                outStr += ""
    except:
        print("Change_Coding_Fail")
    finally:
        if (len(outStr) == 0):
            return "EmptyName"
        else:
            return outStr


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
def get_image_info(path):
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
    return Image(folder_id, folder_name, name, path, type, size, width, height, visit_date, create_date, change_date)

