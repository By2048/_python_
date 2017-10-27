import re
from numpy import *
import numpy as np
import sys

table= '''
元字符	说明
.	匹配任意单个字符
|	逻辑或操作符
[]	匹配字符集合中的一个字符
[^]	对字符集合求非
-	定义一个区间
\	对下一个字符转义
'''






# test='3.1415926'
# print(test.center(20)+'werwer')
# print(test.ljust(20,'=')+'werwer')
# print('{:10s} {:10s}'.format('Hello', 'World')+'rwerwe')

def is_zh_cn(letter):
    if '\u4e00' <= letter <= '\u9fff':
        return True
    else:
        return False

def is_zh_code(symbol):
    codes='！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.'
    if symbol in codes:
         return True
    else:
        return False

def get_zh_cn_num(word):
    num=0
    for letter in word:
        if is_zh_cn(letter):
            num+=1
    return num

def get_zh_code_num(word):
    num=0
    for letter in word:
        if is_zh_code(letter):
            num+=1
    return num

def get_word_length(word):
    num=0
    for letter in word:
        if is_zh_cn(letter):
            num+=2
        if is_zh_code(letter):
            num-=1
        else:
            num+=1
    return num

# 获取列数
def get_tab_num(input_lines):
    first_line=input_lines[0]
    num=len(first_line.split('\t'))
    return num

# 获取每行的长度
def get_all_word_length(input_lines):
    lengths=[]
    for line in input_lines:
        each_line_length=[]
        split_lines=line.split('\t')
        if len(split_lines)==1:
            split_lines=line.split('    ')
        for item in split_lines:
            length=get_word_length(item)
            each_line_length.append(length)
        lengths.append(each_line_length)
    return lengths

# 获取整个输入的最大的行的长度
def get_word_max_lengths(word_lengths):
    max_lengths=[]
    new_length = np.array(word_lengths)
    for num in range(tab_num):
        max_length=max(new_length[:,num])
        max_length+=4
        max_lengths.append(max_length)
    return max_lengths



# def get_second_line():
#     item='    ----'
#     line=''
#     line+='|'
#     for (length,num) in zip(word_max_lengths, range(tab_num)):
#         line+=item.ljust(word_max_lengths[num]+4)+'|'
#     return line




# 获取主体
def get_lines(input_lines,word_max_lengths,tab_num):
    lines=[]
    for each_line in input_lines:
        items=each_line.split('\t')
        if len(items)==1:
            items=each_line.split('    ')
        line=''
        for (item ,num )in zip(items,range(tab_num)):
            line+='|'+' '*4
            line+=item.ljust(word_max_lengths[num]-get_zh_cn_num(item)-get_zh_code_num(item))
        line+='|'
        lines.append(line)
    return lines

# 添加第一,第二行
def add_tab_head(output_lines,tab_num):
    first_line=''
    second_line=''
    for i in range(tab_num):
        first_line+='|'+' '*8
    first_line+='|'

    for i in range(tab_num):
        second_line+='| ------ '
    second_line+='|'
    output_lines.insert(0,second_line)
    output_lines.insert(0,first_line)




if __name__=='__main__':

    tab_num = 0
    word_max_lengths = []
    input_lines = []
    output_lines = []

    # 输入部分
    sentinel = '===='  # 遇到这个就结束
    for line in iter(input, sentinel):
        input_lines.append(line)
    print('\n')

    # 检查输入
    for tab_line in input_lines:
        items=tab_line.split('\t')
        print(len(items),end='    ')
        print(items)
    print('\n')


    tab_num=get_tab_num(input_lines)
    word_lengths=get_all_word_length(input_lines)
    word_max_lengths=get_word_max_lengths(word_lengths)

    # 输出计算的信息
    print('tab_num             '+str(tab_num))
    print('word_lengths        '+str(word_lengths))
    print('word_max_lengths    '+str(word_max_lengths))
    print('\n')

    # 获取主体
    output_lines=get_lines(input_lines,word_max_lengths,tab_num)

    add_tab_head(output_lines,tab_num)

    print('\n'.join(output_lines),end='\n\n')

