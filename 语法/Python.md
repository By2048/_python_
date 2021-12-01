## Python 安装配置

### pip.ini ( 配置 Python pip 使用的镜像源 )
```
path = D:\Python\Lib\site-packages\pip\pip.ini
```

### 更换镜像源
```py
import os
ini="""[global]
index-url = https://pypi.doubanio.com/simple/
[install]
trusted-host=pypi.doubanio.com
"""
pippath=os.environ["USERPROFILE"]+"\\pip\\"
if not os.path.exists(pippath):
    os.mkdir(pippath)
with open(pippath+"pip.ini","w+") as file:
    file.write(ini)
```
