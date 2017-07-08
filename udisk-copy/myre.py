# Coding=utf-8
import re

info= [' 驱动器 H 中的卷是 AM\n', ' 卷的序列号是 4A21-D15A\n']


pattern  = re.compile('是')   #( )(.*?)(\\)

print(pattern.match('驱动器 H 中的卷是 AM\\n'))  # 在起始位置匹配




print(re.match('A','驱动器 H 中的卷是 AM').group())
print(re.match('com','comwww.runcomoob').group())