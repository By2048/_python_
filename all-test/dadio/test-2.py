# 写一个函数，传入一个字符串作为参数，判断如果字符串是数字(0-9)，则返回true，否则返回false。

import re

def is_digit(n):
    re_rule=('\d+')
    if re.match(re_rule,n)==None:
        return False
    else:
        return True





print(is_digit(""))
print(is_digit("7"))
print(is_digit(" "))
print(is_digit("a"))
print(is_digit("a5"))