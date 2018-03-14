import os
import time
import datetime
from PIL import Image as PILImage
import sys


from items import *
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
