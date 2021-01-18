```py
# django日期比较
if challenge.datetime_start <= datetime.now():
TypeError: can't compare offset-naive and offset-aware datetimes

# datetime.datetime.now不是时区感知。
# 使用 timezone.now() 进行比较
from django.utils import timezone
now = timezone.now()
```


代码中添加
`os.environ.setdefault('DJANGO_SETTING_MODULE', 'mydjango.settings')`
`django.setup()`

PyCharm 中添加
`DJANGO_SETTINGS_MODULE`  `{project_name}.settings`
`PYTHONUNBUFFERED`  `1`