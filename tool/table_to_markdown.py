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


tab_num=0
word_max_lengths=[]
input_lines=[]
output_lines=[]

def get_tab_num():
    first_line=input_lines[0]
    num=len(first_line.split('\t'))
    return num


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

def get_word_lengths():
    lengths=[[get_word_length(item) for item in line.split('\t')] for line in input_lines]
    return lengths

def get_word_max_lengths():
    max_lengths=[]
    new_length = np.array(word_lengths)
    for num in range(tab_num):
        max_length=max(new_length[:,num])
        max_length+=4
        max_lengths.append(max_length)
    return max_lengths



def get_second_line():
    item='    ----'
    line=''
    line+='|'
    for (length,num) in zip(word_max_lengths, range(tab_num)):
        line+=item.ljust(word_max_lengths[num]+4)+'|'
    return line



def get_lines():
    lines=[]
    for tab_line in input_lines:
        items=tab_line.split('\t')
        line=''
        for (item ,num )in zip(items,range(tab_num)):
            line+='|'+' '*4
            line+=item.ljust(word_max_lengths[num]-get_zh_cn_num(item)-get_zh_code_num(item))
        line+='|'
        lines.append(line)
    return lines

def add_tab_head(lines):
    new_lines=[]
    new_lines.append(lines[0])
    new_lines.append(get_second_line())
    new_lines+=lines[1:]
    return new_lines



if __name__=='__main__':

    sentinel = '===='  # 遇到这个就结束

    for line in iter(input, sentinel):
        input_lines.append(line)

    print('\n')
    for tab_line in input_lines:
        items=tab_line.split('\t')
        print(items)


    tab_num=get_tab_num()
    word_lengths=get_word_lengths()
    word_max_lengths=get_word_max_lengths()

    print('tab_num             '+str(tab_num))
    print('word_lengths        '+str(word_lengths))
    print('word_max_lengths    '+str(word_max_lengths))

    print('\n')

    output_lines=get_lines()

    # lines=add_tab_head(lines)

    print('\n'.join(output_lines))
    print()

