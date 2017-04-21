import time
import sys
from time import sleep

for i in range(10):
    print (i,end="")
    if(i==2):
        sys.stdout.flush()
    if i == 5:
        sys.stdout.flush()
    time.sleep(0.5)

for i in range(10):
    print (i,end="")
    if(i==2):
        sys.stdout.flush()
    if i == 5:
        sys.stdout.flush()
    time.sleep(0.5)

def viewBar(i):
    output = sys.stdout
    for count in range(0, i + 1):
        second = 0.1
        sleep(second)
        output.write('\rcomplete percent:%.0f%%' % count)
    output.flush()
viewBar(100)

'''
利用标准输出
    先说一下文本系统的控制符：

    \r： 将光标移动到当前行的首位而不换行；

    \n：将光标移动到下一行，并不移动到首位；

    \r\n：将光标移动到下一行首位。
'''

import time
N = 1000
for i in range(N):
    print("进度:{0}%".format(round((i + 1) * 100 / N)), end="\r")
    time.sleep(0.01)
