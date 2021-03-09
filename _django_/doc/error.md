##　python3安装xadmin出现 UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 3444
```
Downloading xadmin-0.6.1.tar.gz (1.0MB)
    100% |████████████████████████████████| 1.0MB 547kB/s
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "C:\Users\leo\AppData\Local\Temp\pip-build-thid_cll\xadmin\setup.py", line 11, in <module>
        long_description=open('README.rst').read(),
    UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 3444: illegal multibyte sequence

    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in C:\Users\leo\AppData\Local\Temp\pip-build-thid_cll\xadmin\
README.rst这个文件的编码有问题，可以内容没什么重要的，可以直接到github上下载安装包，然后新建一个txt空文件，把文件名改成README.rst，替换原来的文件,替换成功后，把压缩包放到一个文件夹中，在命令窗口中进入存放压缩包的文件下，执行pip命令 
```

pip install xadmin-master.zips




## Error: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试。
```
D:\Jetbrains\PyCharm\2017.3\bin\runnerw.exe E:\MyGit\Wallpaper_Website\env\Scripts\python.exe E:/MyGit/Wallpaper_Website/wallpaper/manage.py runserver 8000
Performing system checks...

System check identified no issues (0 silenced).
March 21, 2018 - 08:44:45
Django version 2.0.3, using settings 'wallpaper.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
Error: [WinError 10013] 以一种访问权限不允许的方式做了一个访问套接字的尝试。
```
这种情况就是端口占用

C:\>netstat -ano|findstr 8000  
  TCP    0.0.0.0:8000           0.0.0.0:0              LISTENING       8124  
  UDP    0.0.0.0:8000           *:*                                    8124  
  
C:\>tasklist |findstr 8124  
KGService.exe                 8124 Console                    3     14,480 K  
  
C:\Users\liyunzhi>taskkill /pid 8124 /F  
成功: 已终止 PID 为 8124 的进程。  




## PyCharm 编辑为源文件路径
不使用 app.user  直接使用 user  导入出错问题 no in install_apps



## Exception Value:	(1366, "Incorrect string value: '\\xE6\\x99\\xAE\\xE9\\x80\\x9A...' for column 'nickname' at row 1")
mysql> show create database wallpaper;
+-----------+-------------------------------------------------------------------------------------+
| Database  | Create Database                                                                     |
+-----------+-------------------------------------------------------------------------------------+
| wallpaper | CREATE DATABASE `wallpaper` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */ |
+-----------+-------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

创建数据库的时候选择，utf8 与 utf8_bin

utf-8 utf_general_ci