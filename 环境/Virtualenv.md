- `安装`
    - `pip install virtualenv`
- `创建虚拟环境` 
    - 在当前目录下创建虚拟环境 `virtualenv {name}`
    - 创建时使用系统环境的包 `virtualenv {name} --system-site-packages`
    - 指定版本 `{virtualenv.exe} {name} --python={python.exe}`
- `进入虚拟环境`
    - `Windows` -> `{name}/Scripts/activate.bat` or `.psl`
    - `Linux` -> `source {name}/bin/activate`
- `退出虚拟环境`
    - `deactivate`
- `Demo`
    - `cd /d D:\Python`
    - `D:\Python\3.9.0\Scripts\virtualenv.exe _3.9.0_ --python=D:\Python\3.9.0\python.exe`


```
D:\Python\3.9.6\python.exe -m pip install --upgrade pip

D:\Python\3.9.6\Scripts\pip.exe install virtualenv

D:\Python\3.9.6\Scripts\virtualenv.exe D:\Python\_3.9.6_\ --python=D:\Python\3.9.6\python.exe

D:\Python\_3.9.6_\Scripts\activate.ps1
```