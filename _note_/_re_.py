import re

item = re.split(r'\W+', 'runoob, runoob, runoob.')
print(item)
# ['runoob', 'runoob', 'runoob', '']

item = re.split(r'(\W+)', ' runoob, runoob, runoob.')
print(item)
# ['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']

item = re.split(r'\W+', ' runoob, runoob, runoob.', 1)
# ['', 'runoob, runoob, runoob.']
print(item)

item = re.split(r'a*', 'hello world')  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
print(item)
# FutureWarning: split() requires a non-empty pattern match.
# return _compile(pattern, flags).split(string, maxsplit)
# ['hello world']



# coding=utf-8
import re
import os

lines = []
print(os.getcwd())

_file = None
with open('main.lua', encoding='utf-8') as file:
    _file = "".join(file.readlines())


def replace_config(file, config_name, new_config):
    rule = "(-- start {0} config)([\s\S]+)(-- end {0} config)".format(config_name)
    # print(re.search(rule, file, re.M).groups())
    file = re.sub(rule, new_config, file, re.M)
    return file


new_file = replace_config(_file, 'product_key', 'local product_key="123456"')

with open('main.lua.new', 'w+', encoding='eutf-8') as file:
    print(type(file))
    # file.write(new_file)

# pattern : 一个字符串形式的正则表达式
#
# flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
#
# re.I 忽略大小写
# re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
# re.M 多行模式
# re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
# re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
# re.X 为了增加可读性，忽略空格和 # 后面的注释

"""

在讲 re.compile() 函数时，曾说到该函数还接受可选的第二个参数，用以设置匹配模式。可选的匹配模式有：

re.IGNORECASE：忽略大小写，同 re.I。

re.MULTILINE：多行模式，改变^和$的行为，同 re.M。

re.DOTALL：点任意匹配模式，让'.'可以匹配包括'\n'在内的任意字符，同 re.S。

re.LOCALE：使预定字符类 \w \W \b \B \s \S 取决于当前区域设定， 同 re.L。

re.ASCII：使 \w \W \b \B \s \S 只匹配 ASCII 字符，而不是 Unicode 字符，同 re.A。

"""
