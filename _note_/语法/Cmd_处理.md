
使用 `os.system()` 和 `os.popen()` 执行cmd命令

# os.system
仅仅在一个子终端运行系统命令，而不能获取命令执行后的返回信息

# os.popen
该方法不但执行命令还返回执行后的信息对象

```py
import os

tmps = os.popen('dir').readlines()
for tmp in tmps:
    print(tmp,end='')

def run_cmd(cmd):
    lines=[]
    for line in os.popen(cmd).readlines():
        lines.append(line.replace('''\n''',''))
    for line in lines:
        print(line)

os.system('f:\\test.bat')
```



# 使用模块subprocess
```py
import subprocess
p = subprocess.Popen('dir', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line,)
retval = p.wait()
```