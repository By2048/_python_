## 相关文档
- [GitHub](https://github.com/pyenv/pyenv)
- [wiki](https://github.com/pyenv/pyenv/wiki)
- [Common build problems](https://github.com/pyenv/pyenv/wiki/Common-build-problems)



## 安装
```sh
apt update
apt install libssl1.0-dev -y
apt install make build-essential libssl-dev \
            zlib1g-dev libbz2-dev libreadline-dev \
            libsqlite3-dev wget curl llvm libncurses5-dev \
            xz-utils tk-dev libxml2-dev libxmlsec1-dev \
            libffi-dev liblzma-dev \
            -y

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_aliases
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_aliases
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_aliases
exec "$SHELL"

git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_aliases
exec "$SHELL"

git clone git://github.com/pyenv/pyenv-update.git $(pyenv root)/plugins/pyenv-update
exec "$SHELL"
```



## 命令
|                  |                                   |
|------------------|-----------------------------------|
| 显示所有可用命令 | `pyenv commands`                  |
| 查看可安装版本   | `pyenv install -l`                |
| 安装 / 卸载      | `pyenv install / uninstall 3.7.5` |
| 创建虚拟环境     | `pyenv virtualenv 3.7.5 myenv`    |
|                  |                                   |



## 其他
- 设置`Python`版本
    - 优先级 `shell > local > global`
    - 设置全局`Python`版本，
        - `pyenv global 3.7.5`  
        - 通过将版本号写入 `~/.pyenv/version` 文件的方式 
    - 设置本地`Python`版本，
        - `pyenv local 3.7.5` 
        - 通过将版本号写入当前目录下的 `.python-version` 文件的方式。
- 环境目录 
    - `~/.pyenv/versions`
- 下载加速
    - 下载需要的版本放到 `~/.pyenv/cache` 文件夹下面
    - 执行 `pyenv install 版本号`


