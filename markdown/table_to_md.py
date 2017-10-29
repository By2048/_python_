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
    codes="└＾＜｜〛＼〾〝〃＇＋〜＃〚〿“「、‘＄）【＆】；％＝’…｛｀｠〘﹏｟。＠〔［，－╚／？＞｝〟〰《–—」〙〕］（”〈〉』！·〞『：＂＿〗┐～╗〖》＊"
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
        if is_zh_cn(letter) or is_zh_code(letter):
            num+=2
        # if is_zh_code(letter):
        #     num-=1
        else:
            num+=1
    return num

def splite_items(line):
    splite_tab=line.split('\t')
    splite_space=line.split('    ')
    if len(splite_tab)>len(splite_space):
        items=splite_tab
    elif len(splite_tab)<len(splite_space):
        items=splite_space
    else:
        items=splite_tab
    return items

# 获取列数
def get_tab_num(input_lines):
    first_line=splite_items(input_lines[0])
    num=len(first_line)
    return num

# 获取每行的长度
def get_all_word_length(input_lines):
    lengths=[]
    for each_line in input_lines:
        each_line_length=[]
        split_lines=splite_items(each_line)
        # split_lines=line.split('\t')
        # if len(split_lines)==1:
        #     split_lines=line.split('    ')
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


# 获取主体
def get_lines(input_lines,word_max_lengths,tab_num):
    lines=[]

    first_line=''
    second_line=''
    for (num,word_len) in zip(range(tab_num),word_max_lengths):
        first_line+='|   '+' '*(word_len-3)+'   '
    first_line+='|'
    for (num,word_len) in zip(range(tab_num),word_max_lengths):
        second_line+='|   '+'-'*(word_len-3)+'   '
    second_line+='|'
    lines.append(first_line)
    lines.append(second_line)

    for each_line in input_lines:
        items=splite_items(each_line)
        line=''
        for (item ,num )in zip(items,range(tab_num)):
            line+='|'+' '*3
            line+=item.ljust(word_max_lengths[num]-get_zh_cn_num(item)-get_zh_code_num(item))
        line+='|'
        lines.append(line)
    return lines




if __name__=='__main__':

    tab_num = 0
    word_max_lengths = []
    input_lines = []
    output_lines = []

    # 输入部分
    sentinel = '===='  # 输入以 ==== 结束
    for line in iter(input, sentinel):
        input_lines.append(line)
    print('\n')

    # 检查输入
    for tab_line in input_lines:
        items=splite_items(tab_line)
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

    print('\n'.join(output_lines),end='\n\n')











# ============ Test ===================

# |           |           |
# | --------- | --------- |
# |    Ctrl + Shift + P，F1    |    显示命令面板      |
# |    Ctrl + P                |    快速快开          |
# |    Ctrl + Shift + N        |    新窗口/实例       |
# |    Ctrl + Shift + W        |    关闭窗口/实例     |
# |    Ctrl + K Ctrl +S        |    显示所有快捷键    |
#
# First Header | Second Header
# ------------ | -------------
# Content from cell 1 | Content from cell 2
# Content in the first column | Content in the second column
#
#
# Ctrl + Shift + P，F1	显示命令面板
# Ctrl + P	快速快开
# Ctrl + Shift + N	新窗口/实例
# Ctrl + Shift + W	关闭窗口/实例
# Ctrl + K Ctrl +S	显示所有快捷键
# First Header	Second Header
# Content from cell 1	Content from cell 2
# Content in the first column	Content in the second column

# ============ Test ===================


