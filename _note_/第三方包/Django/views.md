# SQL 操作

## insert 语句：
```
python      p1 = modelsname(列1='xx', 列2='xx') p1.save()      
sql         insert into modelsname (1, 2) value (‘xx', ‘xx')   
```

## select* 以及条件语句
```
作用        select * 表全部数据                                                
python      modelsname.objects.all()                                           
sql         select * from modelsname      

作用        select where 表中符合条件的数据                                    
python      modelsname.objects.filter(name='Apress', name2='abc')          
sql         select * from modelsname where name='Apress' and name2='abc'   

作用        以字段排序      
python      modelsname.objects.order_by('name')                              
sql         select * from modelsname order by name                             

作用        以字段倒序       
python      modelsname.objects.order_by('-name')                             
sql         select * from modelsname order by name desc                        

作用        符合条件的数据 并且执行排序   
python      modelsname.objects.filter(country='U.S.A.').order_by('name')   
sql         select * from modelsname where country='U.S.A.' order by name    

作用        限制返回的数量             
python      modelsname.objects.all()[0]                                        
sql         select * from modelsname limit 1   

作用        根据主键ID获取   
python      modelsname.objects.get(pk=1)                                     
sql         select * from modelsname limit 1                                 
```

## update语句：
python      modelsname.objects.filter(id=52).update(name='Apress Publishing')   
sql         update modelsname set name='Apress Publishing' where id=52          
作用        批量更新           
                                                   
python      modelsname.objects.all().update(country='USA')                      
sql         update modelsname set country='USA'    
作用        将所有的country设置为USA             


## delete语句：
```
python      modelsname.objects.filter(country='USA').delete()   
sql         delete from modelsname where country='USA'
作用        将country==USA 的删除
```


## like语句：
```
__exact         完全匹配                                                                               
python          user.objects.filter(username__exact='xiaobai',password__exact='xiaobai@.com')        
sql             select * from user where name like ‘xiaobai' and password like ‘xiaobai@.com'         
作用            包含匹配     
                                                                             
__contains      部分匹配
python          user.objects.filter(username__contains='xiaobai',password__contains='xiaobai@.com')  
sql             select * from user where name like ‘%xiaobai%' and password like ‘%xiaobai@.com%'     
作用            忽略大小写like like 'xxx'                                                              
```


## 判断语句
```
__year              获取datatime年
__iexact            大小写不敏感匹配
__contains          大小写敏感 匹配
__gt                大于                   
__gte               大于等于               
__lt                小于                   
__lte               小于等于               
__in                存在于一个list范围内   
__startswith        以…开头               
__endswith          以…结尾               
__istartswith       以…开头 大小写不敏感
__iendswith         以…结尾，大小写不敏感  
__range             在…范围内       
```      

# 跨关联关系的查询
Entry.objects.filter(blog__name='Beatles Blog')


# 示例
```py
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
```

## F() Q()
```py
# Django 提供F表达式 来允许这样的比较。 F() 返回的实例用作查询内部对模型字段的引用。 这些引用可以用于查询的filter 中来比较相同模型实例上不同字段之间值的比较。
from django.db.models import F
Entry.objects.filter(n_comments__gt=F('n_pingbacks'))

# Django 支持对F() 对象使用加法、减法、乘法、除法、取模以及幂计算等算术操作，两个操作数可以都是常数和其它F() 对象。
Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))

# F()对象支持位操作.bitand()、.bitor()、.bitrightshift()和.bitleftshift()。 例如：
F('somefield').bitand(16)
```

```py
# 使用Q对象进行复杂查找
# 在filter()中的关键字参数查询 — — 是“AND”的关系。 
# 如果你需要执行更复杂的查询（例如OR 语句），你可以使用Q对象。
Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)
```

[官方文档](https://docs.djangoproject.com/en/1.7/ref/models/queries/)

## @csrf_exempt
使用这个关闭csrf功能

## django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程



        user = request.user
        if user.id == None:
            login = False
        else:
            login = True