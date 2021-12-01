
[Anaconda 官方文档](https://conda.io)



## Linux环境下安装 
```sh
wget https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
chmod +x Anaconda3-5.1.0-Linux-x86_64.sh
./Anaconda3-5.1.0-Linux-x86_64.sh
export PATH=~/anaconda3/bin:$PATH
```


## 命令

查看版本 `conda -V` or `conda --version`

查看帮助 `conda -h` 

安装 `conda install matplotlib`

查看当前环境下已安装的包 `conda list `

更新包 `conda update matplotlib`

删除包 `conda remove matplotlib`

基于 `python3.6` 版本创建一个名字为 `test` 的 `python` 独立环境 `conda create --name test python=3.6`

创建一个名为 `test` 的环境，指定 `python` 版本是 `3.4` （不用管是 `3.4.x` ，`conda` 会为我们自动寻找 `3.4.x` 中的最新版本） `conda create --name test python=3.4`

`Windows`激活某个环境 `activate python34` 
`Linux`激活某个环境 `source activate python34` 

`Windows`退出环境 `deactivate python34`  
`Linux`退出环境 `source deactivate python34` 

删除该环境 `conda remove -n test --all` 或者  `conda env remove  -n test`

查看所有安装的 `python` 环境 `conda info -e`

更新`conda`本身  `conda update conda`

更新`anaconda`应用 `conda update anaconda`

更新`Python`   `conda update python`

## 镜像

添加 `Anaconda` 的镜像

`conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/`
`conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/`

设置搜索时显示通道地址 `conda config --set show_channel_urls yes`

查看某个指定环境的已安装包  `conda list -n python_env`

查找包信息  `conda search numpy`

安装包到制定环境  `conda install -n python_env numpy` 如果不用 `-n` 指定环境名称，则被安装在当前活跃环境

更新制定环境包  `conda update -n python_env numpy`

删除制定环境包  `conda remove -n python_env numpy`

