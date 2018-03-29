# Coding=utf-8
import time
import datetime
import re
import os

print(datetime.datetime.now())

info='''驱动器 X 中的卷是 Backup\n', ' 卷的序列号是 886D-6F6C\n'''
info=info.replace('\n','')
print(info)

# info=re.sub('\S+\s\S\s\S+','',info)

match = re.search(r'(\S{4})(-)(\S{4})',info)
print(match)
print(match.group())



# text = "JGood is a handsome boy, he is cool, clever, and so on..."
# print(re.sub(r'\s+', '-', text))


# path='G:\\Backup\\udisk-copy\\558B-17A2'
# os.makedirs(path)

# computer = keep_path + datetime.datetime.now().strftime("%Y-%m-%d--%H-%M")

