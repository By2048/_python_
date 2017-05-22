import os
import re


class FileInfo:
    num = ''
    old_name = ''
    new_name = ''

    def __init__(self, num, old_name, new_name):
        self.num = num
        self.old_name = old_name
        self.new_name = new_name


file_infos = []


def get_new_name(old_name):
    start_, end_ = os.path.splitext(old_name)
    start_ = re.sub('\[.*\]', "", start_) \
        .replace('.', '') \
        .replace('BD', ' BD ') \
        .replace('HD', ' HD ') \
        .replace('720p', ' 720p ') \
        .replace('  ', ' ') \
        .replace('  ', ' ')
    new_name = start_ + end_
    return new_name


def print_file_info(file_info):
    print('\n')
    print('index      ' + file_info.num)
    print('old_name   ' + file_info.old_name)
    print('new_name   ' + file_info.new_name)
    print('\n')


def insert_file_info():
    index = 1
    dytt_title = re.compile(".*\[(.*)\].*")
    for name in os.listdir(r'f:\video'):
        if re.match(dytt_title, name) is not None:
            num = str(index)
            old_name = 'f:/video/' + name
            new_name = get_new_name(old_name)
            file_info = FileInfo(num, old_name, new_name)
            file_infos.append(file_info)
            print_file_info(file_info)

def input_nums():
    str = input('选择需要重命名的项。。。\n')
    if str.find('.') == -1:
        nums = []
        for num in str[:]:
            nums.append(num)
        return nums
    else:
        return 'all'


if __name__ == '__main__':
    insert_file_info()
    if len(file_infos)==0:
        print('\nNo Find。。。')
        exit(0)
    nums = input_nums()
    if nums == 'all':
        for file_info in file_infos:
            os.rename(file_info.old_name, file_info.new_name)
    else:
        for file_info in file_infos:
            if file_info.id in nums:
                os.rename(file_info.old_name, file_info.new_name)

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
