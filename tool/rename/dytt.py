import os
import re

dytt_title = re.compile(".*\[(.*)\].*")
def get_new_name(old_name):
    start_, end_ = os.path.splitext(old_name)
    start_ = re.sub('\[.*\]', "", start_) \
        .replace('.', '') \
        .replace('BD', ' BD ') \
        .replace('HD', ' HD ') \
        .replace('720p', ' 720p ')\
        .replace('  ',' ')\
        .replace('  ',' ')
    new_name =  start_ + end_
    return new_name

for name in os.listdir(r'f:\video'):
    if re.match(dytt_title, name) is not None:
        old_name = 'f:/video/' + name
        new_name = get_new_name(old_name)
        print('\nold_name   ' + old_name)
        print('new_name   ' + new_name + '\n')
        os.rename(old_name, new_name)