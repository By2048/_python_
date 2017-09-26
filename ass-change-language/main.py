import os
from hanziconv import HanziConv

start_path=r'E:\Desktop\subs test'
change_path=r'E:\Desktop\subs change'


def change_ass(old_path):
    new_path=change_path+'\\'+os.path.basename(old_path)

    old_file = open(old_path, mode='r', encoding='utf-8-sig')
    new_file=open(new_path,mode='w',encoding='utf-8-sig')

    for line in old_file.readlines():
        new_line=HanziConv.toSimplified(line)
        new_file.write(new_line)




# file_path=r'E:\Desktop\1.ass'
#
# file_path_new=r'E:\Desktop\2.ass'
#
# file=open(file_path,mode='r',encoding='utf-8-sig')
#
# file_new=open(file_path_new,mode='w',encoding='utf-8-sig')
#
# for line in file.readlines():
#     new_line=HanziConv.toSimplified(line)
#     file_new.write(new_line)


for path in os.listdir(start_path):
    old_path=start_path+'\\'+path
    change_ass(old_path)