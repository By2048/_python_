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
