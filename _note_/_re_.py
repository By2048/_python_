import re

from _tool_._other_ import run_all_test, log
from _tool_._decorator_ import run_time, log_test


@log_test
def test_1():
    item_1 = re.split(r'\W+', 'runoob, runoob, runoob.')
    item_2 = re.split(r'(\W+)', 'runoob, runoob, runoob.')
    item_3 = re.split(r'\W+', 'runoob, runoob, runoob.', 1)
    # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
    """    
    def split(pattern, string, maxsplit=0, flags=0):
        return _compile(pattern, flags).split(string, maxsplit)
    """
    item_4 = re.split(r'a*', 'hello world')
    # log(locals())


# def test_2():
# file = ""
# rule = "(-- start {0} config)([\s\S]+)(-- end {0} config)".format("config name")
# item = re.search(rule, file, re.M).groups()
# file = re.sub(rule, "new_config", file, re.M)
# pass


if __name__ == '__main__':
    # print(test_1.__code__)
    run_all_test(globals())

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


# pattern : 一个字符串形式的正则表达式#
# flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
#
# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式
# re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X 为了增加可读性，忽略空格和 # 后面的注释

# def test_3():
#     item_1 = "egerg455hert985".find('.')
#     log(locals())
