```py
import glob
# 用它可以查找符合特定规则的文件路径名
# 查找文件只用到三个匹配符："*", "?", "[]"。
# "*"匹配0个或多个字符；
# "?"匹配单个字符；
# "[]"匹配指定范围内的字符，


glob.glob(r'f:\image\*.jpg')
# ['f:\\image\\52.jpg', 'f:\\image\\13.jpg', 'f:\\image\\47.jpg', 'f:\\image\\eye.jpg']


# glob.iglob
# 获取一个可编历对象，使用它可以逐个获取匹配的文件路径名。
# 与glob.glob()的区别是：glob.glob同时获取所有的匹配路径，
# 而 glob.iglob一次只获取一个匹配路径。
file=glob.iglob(r'f:\image\*.jpg')
print(file)
# <generator object _iglob at 0x0032D120>

for item in file:
    print(item)
# f:\image\52.jpg
# f:\image\13.jpg
# f:\image\47.jpg
# f:\image\eye.jpg
```