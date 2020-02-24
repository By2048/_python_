import os
import re

start_path = 'F:\\Download'


def get_name(name):
    data = [
        ('阳光电影', ''),
        ('www.ygdy8.com', ''),
        ('中英双字幕', ''),
        ('国英双语双字', ''),
        ('国印双语中字', ''),
        ('.', ''),
        (':', ' '),
        ('：', ' '),
        ('BD', ''),
        ('HD', ''),
        ('720p', ''),
    ]
    _start, _end = os.path.splitext(name)  # xxx | .xxx
    for item in data:
        _start = _start.replace(item[0], item[1])
    return f"{_start}{_end}"


def init():
    result = []
    for item in os.listdir(start_path):
        if not item.endswith('.mkv'):
            continue
        result.append([os.path.join(start_path, item), os.path.join(start_path, get_name(item))])
    return result


if __name__ == '__main__':
    data = init()
    if not data:
        print('\nNo Find。。。')
        exit(0)

    for index, item in enumerate(data, 1):
        print(f"{index}   {item[0].lstrip(start_path)}  |->|  {item[1].lstrip(start_path)}")

    cmd = input('\n选择需要重命名的项 [123]每位分割 [.]重命名所有\n\n')
    if cmd == '0':
        exit()
    elif cmd == '.':
        for item in data:
            os.rename(item[0], item[1])
    else:
        cmd = [int(item) for item in list(cmd) if item.isdigit()]
        for index, item in enumerate(data, 1):
            if index in cmd:
                os.rename(item[0], item[1])

# old_str="egerg455hert985"
# print(old_str.find('.'))
#
# num=re.findall(r'\d',old_str)
# print(num)
#
# is_num = re.compile('\d{1,4}')
# print(is_num.findall(old_str))
#
# new_str=re.sub(r'\d{1,2}', '', old_str)
# print(new_str)

# [0 - 9]
# print(re.match([0-9]),str)

# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
#
# print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配

# phone = "2004-959-559 # 这是一个电话号码"
#
# # 删除注释
# num = re.sub(r'#.*$', "", phone)
# print("电话号码 : ", num)
#
# # 移除非数字的内容
# num = re.sub(r'\d', "", phone)
# print("电话号码 : ", num)
