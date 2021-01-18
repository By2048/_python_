## 命令

- 显示所有安装的包
    - `pip list` 
    - `pip freeze`
- 更新 
    - `pip install -U {name}` 
    - `pip install --upgrade {name}`
- 使用源码安装 
    - `python setup.py install`
- 卸载 
    - `pip uninstall package_name`
- 卸载所有
    - `pip freeze | xargs pip uninstall -y`
- 安装 `requirements.txt` 依赖
    - `pip install -r requirements.txt`
- 生成依赖
    - `pip freeze > requirements.txt`
- 安装`whl`包
    - `pip install {name}`
    - `pip install {package_name}.whl`
- 查看可以升级的安装包
    - `pip list --outdated --format=columns` 
    - 选项
        - `columns`
        - `freeze`
        - `json`


 
## 镜像源

- 豆瓣    
    - `http://pypi.douban.com/simple/`
- 清华
    - `https://pypi.tuna.tsinghua.edu.cn/simple`
- 临时使用镜像源安装 
    - `pip install tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple`

修改环境

`Linux`下，修改 `~/.pip/pip.conf` (没有就创建一个)，内容如下：

```conf
[global]
trusted-host =  mirrors.aliyun.com
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

`Windows`下，直接在`user`目录中创建一个`pip`目录，如：`C:\Users\xx\pip`，新建文件`pip.ini`，内容如下

```conf 
[global]
trusted-host =  mirrors.aliyun.com
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```