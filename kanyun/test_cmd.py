import os

tmps = os.popen('dir').readlines()
for tmp in tmps:
    print(tmp,end='')
