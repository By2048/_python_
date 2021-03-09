# manage 

## 命令

- `django-admin startproject mysite` 这将会在你的当前目录下生成一个 mysite 项目
- `python** manage.py` 查看所有的帮助
- `python manage.py startapp blog` 创建app模块
- `python manage.py runserver` 运行服务
- `python manage.py runserver 9999` 运行服务并设置端口
- `python manage.py runserver 0.0.0.0:8000` 运行服务并设置端口 IP
- `python manage.py makemigrations` + `app_name` 根据model创建表的生成文件
- `python manage.py migrate` + `app_name` 表的迁移 保存到数据库
- `python manage.py sqlmigrate blog 0001` 查看数据库创建语句
- `python manage.py createsuperuser` 创建管理员用户
- `python manage.py shell` 测试diango中的方法
- `python manage.py rebuild_index` 就可以建立索引文件了
- `python manage.py validate` 检查模型有效性
- `python manage.py showmigrations` 查看迁移文件

> - `migrations` 相当一个你的数据库的一个版本控制系统
> - `makemigrations` 命令负责保存你的模型变化到一个迁移文件 和 `commits` 很类似  
> - `migrate` 负责将改变提交到数据库。


## 使用`shell`来测试

```py
>>> from blog.models import Article
>>> Article.objects.all()
```

# 其他

## 使用现有的数据库创建`model`
```sh
python manage.py inspectdb    # 在控制台查看创建的模型
python manage.py inspectdb > app/models.py   # 模型导出到文件
```

## `app`文件夹
- 如果创建应用比较多，可以创建一个`app`的文件夹 ，把所有应用放在里面，
- 但这样会要求有`import`时前面加上一个`app`
- 在`PyCharm`中把`apps`右键`Mark`为`Sources Root`
- 或者在`settings.py`中加入以下代码
```py
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
```

# 测试django的版本
`import django; print(django.get_version())`

