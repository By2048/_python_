

http://usyiyi.cn/translate/Django_111/howto/static-files/index.html

你的项目可能还有一些静态文件不属于任何一个特定的应用。 除了在应用中使用static/目录，你还可以在settings文件中定义一个目录列表（STATICFILES_DIRS），Django会在其中查找静态文件。 像这样：
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]
```