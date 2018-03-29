# Java编程思想中 对源码进行一些修改（去除头部的信息）
import re
import os


replace_str_1= '''/* Added by Eclipse.py */'''
change_str_1= ''

replace_str_2= '''//i'''
chnage_str_2= '''// i'''

replace_str_3= '''} /*'''
change_str_3= '} \n\n/*'

# 源码的路径
start_path="E:\Desktop\TIJ4-code\src\main\java"


matchObj = re.compile('\t \*',re.S)


def replace_file(old_path,new_path):
    with open(old_path) as file:
        lines = file.readlines()
    with open(new_path, 'w') as file:
        for line in lines:
            if replace_str_1 in line:
                line = line.replace(replace_str_1, change_str_1)
            if replace_str_2 in line:
                line = line.replace(replace_str_2, chnage_str_2)
            if replace_str_3 in line:
                line = line.replace(replace_str_3, change_str_3)
            if matchObj.match(line) != None:
                span_end = matchObj.match(line).span()[1]
                file.write(' *' + line[span_end:])
                continue
            file.write(line)


def start_replace():
    for root, dirs, files in os.walk(start_path):
        if len(files) == 0:
            pass
        for file in files:
            if file.endswith('.java'):
                old_path = os.path.join(root, file)
                back_path = os.path.join(root, '-'+file)
                os.rename(old_path,back_path)
                replace_file(back_path,old_path)
                os.remove(back_path)
                print(old_path)


if __name__=='__main__':
    start_replace()