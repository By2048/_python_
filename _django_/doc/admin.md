[Admin 官方文档](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/)

```py
from django.db import models
from django.contrib import admin

class Person(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()

    def decade_born_in(self):
        return self.birthday.strftime('%Y')[:3] + "0's"
    decade_born_in.short_description = 'Birth decade'

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'decade_born_in')
```

```py
def upper_case_name(obj):
    return ("%s %s" % (obj.first_name, obj.last_name)).upper()
upper_case_name.short_description = 'Name'

class PersonAdmin(admin.ModelAdmin):
    list_display = (upper_case_name,)
```

```py
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
```

```py
class PersonAdmin(admin.UserAdmin):
    list_filter = ('company__name',)
```


```py
from django.contrib import admin
from blog.models import Blog
  
## Blog模型的管理器
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    #listdisplay设置要显示在列表中的字段（id字段是Django模型的默认主键）
    list_display = ('id', 'caption', 'author', 'publish_time')
    
    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 50
    
    #ordering设置默认排序字段，负号表示降序排序
    ordering = ('-publish_time',)
  
    #list_editable 设置默认可编辑字段
    list_editable = ['machine_room_id', 'temperature']
  
    #fk_fields 设置显示外键字段
     fk_fields = ('machine_room_id',)
```