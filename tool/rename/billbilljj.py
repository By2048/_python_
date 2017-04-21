import os
import re

start_path = r'f:\video\MMD\MMD'
for name in os.listdir(start_path):
    old_name = os.path.join(start_path, name)
    new_name = old_name\
        .replace('【', '[')\
        .replace('】', ']') \
        .replace('BilibiliJJ.COM-[MMD]', '') \
        .replace('_', '')\
        .replace('[MMD]','')\
        .strip()
    print('old_name   ' + old_name)
    print('new_name   ' + new_name + '\n')
    os.rename(old_name, new_name)
