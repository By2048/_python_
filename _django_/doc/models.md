# `Django` 模型

## 所有的数据类型
```py
__all__ = [
    'AutoField', 'BLANK_CHOICE_DASH', 'BigAutoField', 'BigIntegerField',
    'BinaryField', 'BooleanField', 'CharField', 'CommaSeparatedIntegerField',
    'DateField', 'DateTimeField', 'DecimalField', 'DurationField',
    'EmailField', 'Empty', 'Field', 'FieldDoesNotExist', 'FilePathField',
    'FloatField', 'GenericIPAddressField', 'IPAddressField', 'IntegerField',
    'NOT_PROVIDED', 'NullBooleanField', 'PositiveIntegerField',
    'PositiveSmallIntegerField', 'SlugField', 'SmallIntegerField', 'TextField',
    'TimeField', 'URLField', 'UUIDField',
]
```
## 常用Models数据类型

`DateTimeField`和`DateField`和`TimeField`存储的内容分别对应着`datetime()`,`date()`,`time()`三个对象。

`auto_now=Ture`，字段保存时会自动保存当前时间，但要注意每次对其实例执行`save()`的时候都会将当前时间保存，也就是不能再手动给它存非当前时间的值。

`auto_now_add=True`，字段在实例第一次保存的时候会保存当前时间，不管你在这里是否对其赋值。
但是之后的`save()`是可以手动赋值的。也就是新实例化一个model，想手动存其他时间，就需要对该实例`save()`之后赋值然后再`save()`。


## Model 示例
```py
from django.db import models

class ModelName(models.Model):
    _sexs = (
            ('1', '男'),
            ('0', '女'),
            ('-1', '中'),
    )
    id = models.CharField(primary_key=True, max_length=10, verbose_name='用户ID')
    name = models.CharField(max_length=50, verbose_name='用户名')
    image = models.ImageField(upload_to='image/%Y/%m', default='/static/image/default.png', max_length=100, verbose_name='头像')
    sex = models.CharField(max_length=10, choices=_sexs,default='-1', verbose_name='性别')
    
    class Meta:
        db_table = 'db_user'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name 
    
    ## 在后台可以显示用户名为key的信息    
    def __str__(self):
        return self.username   
```




## `Django Meta` 选项
```py
# 通过一个内嵌类 "class Meta" 给你的 model 定义元数据, 类似下面这样:
class User(models.Model): 
    name = models.CharField(maxlength=30)
    class Meta: 
        # ...
```
Model 元数据就是 "不是一个字段的任何数据" -- 比如排序选项, admin 选项等等.

[Meta 官方文档（1.82）](http://python.usyiyi.cn/documents/django_182/ref/models/options.html)

`db_table = "user"`
若不提供该参数, `Django` 会使用 `app_label + '_' + module_name` 作为表的名字.
若你的表的名字是一个 SQL 保留字, 或包含 Python 变量名不允许的字符--特别是连字符 --没关系. Django 会自动在幕后替你将列名字和表名字用引号引起来.

`get_latest_by`
一个 DateField 或 DateTimeField 字段的名字. 若提供该选项, 该模块将拥有一个 get_latest() 函数以得到 "最新的" 对象(依据那个字段)`get_latest_by = "order_date"`

`ordering`
默认排序字段及排序方式, 用于得到一个对象列表的任何场合:`ordering = ['-order_date']`

这是一个 tuple 或一个字符串列表. 每个字符串是一个字段名带及一个可选的前缀 "-" , 这个前缀表示按降序排序(递减). 若没有这个前缀,则表示按升序排序.字符串 "?" 表示随机排序.

举个例子, 要对 pub_date 字段以升序排列, 这样做:`ordering = ['pub_date']`要降序排列, 这样:`ordering = ['-pub_date']`要对 pub_date 降序,然后对 author 升序, 这样:`ordering = ['-pub_date', 'author']`

注意一点,不论你使用了多少个字段排序, admin 只使用第一个字段.

`db_table`
`db_table = 'music_album'`
本模块在数据库中对应的表的名字:

`verbose_name`
对象的一个易于理解的名称，为单数：
`verbose_name = "pizza"`

`verbose_name_plural`
对象名字的复数 若未提供该选项, Django 会使用 verbose_name + "s"
`verbose_name_plural = "stories"`


## ManyToManyField 使用
```py
from django.db import models  
  
class Publisher(models.Model):  
    name = models.CharField(max_length=30)  
    address = models.CharField(max_length=50)  
    city = models.CharField(max_length=60)  
    state_province = models.CharField(max_length=30)  
    country = models.CharField(max_length=50)  
    website = models.URLField()  
  
class Author(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=40)  
    email = models.EmailField()  
  
class Book(models.Model):  
    title = models.CharField(max_length=100)

    # 一本书有多个作者，一个作者有多本书 使用 ManyToManyField
    authors = models.ManyToManyField(Author)

    # 一本书只有一个出版社 使用 ForeignKey
    publisher = models.ForeignKey(Publisher)  

    publication_date = models.DateField()  
```

## Django 查询对应的 SQL 语句

```sql
SQL
begin;  
create table "books_publisher" (  
    "id" serial not null primary key,  
    "name" varchar(30) not null,  
    "address" varchar(50) not null,  
    "city" varchar(60) not null,  
    "state_province" varchar(30) not null,  
    "country" varchar(50) not null,  
    "website" varchar(200) not null  
);  
create table "books_author" (  
    "id" serial not null primary key,  
    "first_name" varchar(30) not null,  
    "last_name" varchar(40) not null,  
    "email" varchar(75) not null  
);  
create table "books_book" (  
    "id" serial not null primary key,  
    "title" varchar(100) not null,  
    "publisher_id" integer not null references "books_publisher" ("id") deferrable initially deferred,  
    "publication_date" date not null  
);  

-- 使用 ManyToManyField 时多创建的一个表
create table "books_book_authors" (  
    "id" serial not null primary key,  
    "book_id" integer not null references "books_book" ("id") deferrable initially deferred,  
    "author_id" integer not null references "books_author" ("id") deferrable initially deferred,  
    unique ("book_id", "author_id")  
);  
create index "books_book_publisher_id" on "books_book" ("publisher_id");  
commit; 
```

```py
# book_authors表是关联表，不能直接插入数据，不存在叫做BookAuthors的对象
# 所以要插入这里面数据，建立起book和author的联系时，必须取出book实例，并给book赋值 

# 首先是创建一个book，book创建之后才能添加联系表，这是显然的  
book = Book()  
book.save()

# 添加三个作者，
book.authors = Author.objects.all()[0:3]  
# 或者添加一个作者，传入一个实例  
book.authors.add(Author.objects.all()[0])  
book.save()

# ManyToManyField 的好处是不是就是省去了创建一个简单联系表
# 使用它我们还可以做到通过把一张表中某键值在另一张表中全部映射的对象找出来。
# 比如把某书的所有作者，或者某作者的所有书找出来。 
 book.authors.all () 
 author.book_set.all () 
```

``` sql 
-- 如果用三张表的方法：一个 publisher ，一个 author ，一个 publisher_author ，
--.PublisherAuthor 模型不指定 ManyToManyField 而只用 ForeignKey 
-- 查出 publisher.author 对应的 PublisherAuthor 对象 相当与只执行了 
 select  publisher_author .* 
 from  publisher_author.author 
 where  publisher_author.author_id.author.id  
-- 通过 author.id 找出真正的 author.


-- ManyToManyField
select * from publisher 
where publisher.id in (select publisher_id 
                       from publisher_author, author 
                       where publisher_author.author_id = author.id) 
```


## on_delete在Django模型上做了什么？
`image = models.ForeignKey(Image, null=True, verbose_name='图片', on_delete=models.CASCADE)`

这是删除引用对象时要采用的行为。它不是特定于django，这是一个SQL标准。发生此类事件时可采取以下6种行动：

`CASCADE`：删除引用的对象时，也删除引用它的对象（例如，当您删除博客文章时，您可能也想删除博客讨论）。SQL相当于：`CASCADE`
`PROTECT`：禁止删除引用的对象。要删除它，你必须删除手动引用它的所有对象。SQL相当于：`RESTRICT`
`SET_NULL`：将引用设置为NULL（要求该字段为空）。例如，当你删除一个用户时，你可能想保留他发布在博客文章上的评论，但是说它是由匿名（或删除的）用户发布的。SQL相当于：`SET NULL`
`SET_DEFAULT`：设置默认值。SQL相当于：`SET DEFAULT`
`SET(...)`：设定一个给定的值。这不是SQL标准的一部分，完全由Django处理
`DO_NOTHING`：可能是一个非常糟糕的想法，因为这会在数据库中创建完整性问题（引用实际上不存在的对象）。SQL相当于：`NO ACTION`



```py
# 不使用 Django 内置的 user
# class User(models.Model):
#     _sex = (
#         ('1', '男'),
#         ('0', '女'),
#         ('-1', '中'),
#     )
#     _type = (
#         ('0', 'default'),
#         ('1', 'vip'),
#     )
#     id = models.AutoField(primary_key=True, verbose_name='用户ID')
#     username = models.CharField(max_length=50, default='', verbose_name='用户名')
#     password = models.CharField(max_length=50, verbose_name='密码')
#     image = models.ImageField(upload_to='resource/user_image', default='/static/resource/user_image/default.png',
#                               null=True, blank=True, verbose_name='头像')
#     email = models.EmailField(max_length=50, verbose_name='邮箱')
#     is_active = models.BooleanField(default=False, verbose_name='用户是否可以使用')
#     sex = models.CharField(max_length=10, choices=_sex, default='中', null=True, blank=True, verbose_name='性别')
#     birthday = models.DateField(max_length=10, null=True, blank=True, verbose_name='生日')
#     address = models.CharField(max_length=100, null=True, blank=True, verbose_name='地址')
#     phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
#     information = models.TextField(null=True, blank=True, verbose_name='信息')
#     date_joined = models.DateTimeField(default=datetime.now, verbose_name='注册时间')
#
#     last_login = models.DateTimeField(default=datetime.now, verbose_name='最后登录时间')
#     type = models.CharField(max_length=50, choices=_type, default='0', verbose_name='用户类型')
#     integral = models.IntegerField(default=100, verbose_name='用户积分')
#
#     class Meta():
#         db_table = 'db_user'
#         verbose_name = '用户信息'
#         verbose_name_plural = verbose_name
#
#     # 自定义显示的信息
#     def __str__(self):
#         return '{0}({1})'.format(self.username, self.email)
```


def clear_sql():
    pass


# str = "[www.runoob.com]"
#
# print ("str.center(40, '*') : ", str.center(40, ' '))