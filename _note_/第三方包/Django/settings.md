# 链接数据库使用 `pymysql`
```py
# Project __init__.py
# 设置适应pymysql进行数据库操作
import pymysql
pymysql.install_as_MySQLdb()
```


## 配置MySQL数据库链接
```py
# 使用 apps 时添加到搜索路径
sys.path.insert(0, os.path.join(BASE_DIR, 'app'))

# 配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'diango_test',
        'USER':'root',
        'PASSWORD':'admin',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'CHARSET':'utf8'
    }
}

## 添加包
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appname'
]

# 自定义的用户登陆
AUTHENTICATION_BACKENDS = (
    'user.views.CustomBackend',
)

# 使用自定义的User
AUTH_USER_MODEL = 'user.UserProfile'

# 配置语言
LANGUAGE_CODE = 'zh_Hans'

# 配置时区
TIME_ZONE = 'Asia/Shanghai'

# 使用本地时间为不是UTC
USE_TZ = False

# 配置邮箱
EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'byamend@sina.com'
EMAIL_HOST_PASSWORD = 'ljxl12'
EMAIL_USE_TLS = False
EMAIL_FROM = 'byamend@sina.com'

# 配置 static 文件的根路径
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


```


`django.contrib.admin`  管理站点。 

`django.contrib.auth`  认证系统。

`django.contrib.contenttypes`  用于内容类型的框架。

`django.contrib.sessions`  会话框架。

`django.contrib.messages`  消息框架。

`django.contrib.staticfiles`  管理静态文件的框架。




