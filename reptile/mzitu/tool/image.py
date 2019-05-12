# coding=utf-8
import os
import time
import datetime

from PIL import Image as PILImage

try:
    from mzitu.tool.model import MFolder, MImage
except ImportError:
    from tool.model import MFolder, MImage


def change_name(name):
    """ 编码转换去除系统不允许的字符

    Win系统不允许的文件名 \ / : * ? ' < > |             \n
    操作系统限制 使用特殊标记替换字符 方便后期恢复       \n
    question_mark(?)                                   \n
    colon_mark(:)                                      \n

    :param name: 需要转换的文件名
    :return: 转换后的文件名
    """

    replaces = {
        '？': '(qm)',
        '?': '(qm)',
        ':': '(cm)',
    }
    removes = ['\\', '/', '*', '\'', '<', ' > ', '|', ]

    for key, value in replaces.items():
        name = name.replace(key, value)

    for item in removes:
        name = name.replace(item, ' ')

    return name.strip()


def get_folder_info(folder_path: str) -> MFolder:
    """ 获取图片文件夹的信息  文件夹名 路径 创建时间 文件夹内图片数量 文件的大小

    :param folder_path: 文件夹的绝对路径
    :return: 文件夹的大小 单位 M
    """

    def get_size_num(start_path):
        total_size, image_num = 0, 0
        image_types = ['.jpg', '.png', '.gif', '.jpeg']
        for dirpath, dirnames, filenames in os.walk(start_path):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                total_size += os.path.getsize(file_path)
                file_type = os.path.splitext(file)[1].lower()
                if file_type in image_types:
                    image_num += 1

        return round(total_size / 1024 / 1204, 2), image_num

    create_date = datetime.datetime.fromtimestamp(os.path.getctime(folder_path))
    create_date = create_date.strftime('%Y-%m-%d %H:%M:%S')

    total_size, image_num = get_size_num(folder_path)
    folder_name = os.path.basename(folder_path)

    return MFolder(folder_name, folder_path, create_date, image_num, total_size)


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


# def get_image_info(path):
#    # 获取图片文件具体信息
#     name = os.path.basename(path)
#     folder_name = os.path.splitext(path)[0].split('\\')[-2]
#     folder_id = get_folder_id(sql_server_con_text, folder_name)
#     type = os.path.splitext(path)[1].replace('.', '')
#     size = int(os.path.getsize(path) / 1024)
#     atime = os.path.getatime(path)  # 文件最后访问时间
#     ctime = os.path.getctime(path)  # 文件创建时间
#     mtime = os.path.getmtime(path)  # 文件最后修改时间
#     _atime = time.localtime(atime)
#     _ctime = time.localtime(ctime)
#     _mtime = time.localtime(mtime)
#     visit_date = str(_atime[0]) + '-' + str(_atime[1]) + '-' + str(_atime[2]) + ' ' + \
#                  str(_atime[3]) + ':' + str(_atime[4]) + ':' + str(_atime[5])
#     create_date = str(_ctime[0]) + '-' + str(_ctime[1]) + '-' + str(_ctime[2]) + ' ' + \
#                   str(_ctime[3]) + ':' + str(_ctime[4]) + ':' + str(_ctime[5])
#     change_date = str(_mtime[0]) + '-' + str(_mtime[1]) + '-' + str(_mtime[2]) + ' ' + \
#                   str(_mtime[3]) + ':' + str(_mtime[4]) + ':' + str(_mtime[5])
#     width, height = PILImage.open(path).size[0], PILImage.open(path).size[1]
#     return MImage(folder_id, folder_name, name, path, type, size, width, height, visit_date, create_date,
#                   change_date)


if __name__ == '__main__':
    change_name('')
    get_folder_info("/home/am/Downloads")
