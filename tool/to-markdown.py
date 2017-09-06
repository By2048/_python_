import re

info='''元字符	说明
.	匹配任意单个字符
|	逻辑或操作符
[]	匹配字符集合中的一个字符
[^]	对字符集合求非
-	定义一个区间
\	对下一个字符转义'''

def get_tb_num():
    first_line=info.split('\n')[0]
    num=len(first_line.split('\t'))
    print(num)

# for line in info.split('\n'):
#     print(line.split('\t'))

print(get_tb_num())

test='3.1415926'

print(test.center(20)+'werwer')

print(test.ljust(20,'=')+'werwer')



print('{:10s} {:10s}'.format('Hello', 'World')+'rwerwe')

def get_zh_cn_num(word):
    num=0
    for letter in word:
        if '\u4e00'<=letter<='\u9fff':
            num+=1
    print(num)

pd=True
for line in info.split('\n'):
    items=line.split('\t')
    if pd==True:
        print('{:17s}'.format(items[0]),end='')
        print('{:20s}'.format(items[1]))
        pd=False
    else:
        print('{:20s}'.format(items[0]), end='')
        print('{:20s}'.format(items[1]))

get_zh_cn_num('元jgfffd字2548768768%#@$@%$@#%@$符')