# 页面的模板
```html
<!-- base.html -->
<p>书名：{% block title %}书名（请自定义）{% endblock %}</p>
<p>作者：{% block author %}作者名（请自定义）{% endblock %}</p>

<!-- exrend base.html -->
{% extends "base.html" %}
{% block title %}红楼梦{% endblock %}
{% block author %}曹雪芹{% endblock %}

用 {{ block.super }} 获取父模板 block 内容：
{% block author %} {{ block.super }} {% endblock %}

<!-- 父模板 block 增加新内容 -->
{% block author %} {{ block.super }}新增加的内容 {% endblock %}
```

```html
使用include标记来引入重复的文件的部分

<!-- header.html: -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">  
<html lang="en">  
<head> 

<!-- footer.html: -->
<hr>  
<p>Thanks for visiting my site.</p>  
</body>  
</html>  

<!-- content.html -->
{% include 'header.html' %}  
this is some text of index
{% include 'footer.html' %}  
```

# 模板语言

用 `{{ }}` 包围的是变量 `{{ person_name }}` ，这表示把给定变量的值插入

用 `{% %}` 包围的是块标签 `{% if ordered %}`


# 模板示例
```py
mylist = [(a, b, c), (x, y, z), (l, m, n)]

{% for item in mylist %}    
     {{ item.0 }} {{ item.1}} {{ item.2 }}    
{% endfor %}
```


注意{{ article.pub_date|date:"F j, Y" }}使用Unix风格的“管道”（“|”字符）。 这叫做模板过滤器，


<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>

<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>

forloop.counter指示for标签已经循环多少次。

{{ name|upper }}  {# 大写 #}


# 自定义404，500页面
在templates目录下新建404.html，500.html两个文件
`DEBUG`修改为`False`
`ALLOWED_HOSTS`添加指定域名或者IP
指定模板路径`‘DIRS:
[os.path.join(BASE_DIR,'templates')]`

DEBUG = False`
ALLOWED_HOSTS = ['localhost','www.example.com', '127.0.0.1']

```py
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def hello(request):
    return HttpResponse('Hello World!')

@csrf_exempt
def page_not_found(request):
    return render_to_response('404.html')


@csrf_exempt
def page_error(request):
    return render_to_response('500.html')


from django.conf.urls import url
from django.contrib import admin
import HelloWorld.views as view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test$', view.hello),
]
handler404 = view.page_not_found
handler500 = view.page_error
```

# 模板标签


## autoescape
控制自动转义是否可用. 这种标签带有任何 on 或 off 作为参数的话，他将决定转义块内效果。 该标签会以一个endautoescape作为结束标签.
当自动转义生效时，所有变量内容会被转义成HTML输出（在所有过滤器生效后） 这等同与手动将escape筛选器应用于每个变量。
唯一一个例外是，变量或者通过渲染变量的代码，或者因为它已经应用了 safe或escape过滤器，已经被标记为“safe”。
```
{% autoescape on %}
    {{ body }}
{% endautoescape %}
```


# 过滤器

过滤器看起来是这样的：{{ name|lower }}。 这将在变量 {{ name }} 被过滤器 lower 过滤后再显示它的值，该过滤器将文本转换成小写。 使用管道符号 (|)来应用过滤器。
过滤器可以“链接”。一个过滤器的输出应用于下一个过滤器。 {{ text|escape|linebreaks }} 就是一个常用的过滤器链，它编码文本内容，然后把行打破转成<p> 标签。
一些过滤器带有参数。 过滤器的参数看起来像是这样： {{ bio|truncatewords:30 }}。 这将显示 bio 变量的前30个词。


# {{ value|default:"nothing" }}
如果一个变量是false或者为空，使用给定的默认值。 否则，使用变量的值。 

# {{ value|length }}
返回值的长度。 它对字符串和列表都起作用。 

# {{ value|filesizeformat }}
格式化为“人类可读”文件大小（即'13 KB'，t4> MB'，'102 bytes'等）。 
value 是 123456789，输出将会是 117.7 MB



# 自定义模板标签和过滤器
例如，你的自定义标签/过滤器在一个名为poll_extras.py的文件中，那么你的app目录结构看起来应该是这样的：
```
polls/
    __init__.py
    models.py
    templatetags/
        __init__.py
        poll_extras.py
    views.py
```

{% load poll_extras %}
为了让{% load %} 标签工作，包含自定义标签的应用必须在INSTALLED_APPS中。


为了成为一个可用的标签库，这个模块必须包含一个名为 register的变量，它是template.Library 的一个实例，所有的标签和过滤器都是在其中注册的。 所以把如下的内容放在你的模块的顶部：

```py
from django import template
register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')
{{ somevariable|cut:"0" }}

@register.filter
# 将使用函数名作为过滤器
def lower(value): # Only one argument.
    """Converts a string into a"""

@register.filter(is_safe=True)
# 自动转义处理 HTML 不安全字符（<、'、>、" 或&）
def myfilter(value):
    return value
# 输入没有标记为“安全”，Django 将对输出进行转义。
```





句点查找规则可概括为： 当模板系统在变量名中遇到点时，按照以下顺序尝试进行查找：

字典类型查找 （比如 foo["bar"] )

属性查找 (比如 foo.bar )

方法调用 （比如 foo.bar() )

列表类型索引查找 (比如 foo[bar] )

如何处理无效变量
默认情况下，如果一个变量不存在，模板系统会把它展示为空字符串，不做任何事情来表示失败。 例如：


Python 的“真值”

在Python和Django模板系统中，以下这些对象相当于布尔值的False

空列表([] )

空元组(() )

空字典({} )

空字符串('' )

零值(0 )

特殊对象None

对象False（很明显）

提示：你也可以在自定义的对象里定义他们的布尔值属性(这个是python的高级用法)。