## url 示例文件

```py
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    # 设置 namespace 来使用 namespace:url_name 来链接网页
    url(r'^blog/', include('blog.urls',namespace='blog')),
]


urlpatterns = [
    # 使用空参数
    url(r'^$', views.index),

    # 使用正则表达式来匹配视图
    url(r'^index/$', views.index),

    # url 自定义名字
    url(r'^edit/action/$', views.edit_action,name='edit_action'),

    # 指定参数名
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),

    # 使用多个参数
    url(r'^edit/(?P<passcode>.*)/(?P<article_id>.*)/(?P<title>.*)/(?P<content>.*)/$', view=edit_article),
]

```


## 其他
### 网络爬虫访问
```py
url(r'^robots\.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')),
```


### 获取当前页面的 URL
获取带参数URL`request.get_full_path()`
获取不带参数URL`request.path`
获取主机地址`request.get_host()`




## 通过URL传递参数

### 默认进行匹配
```py
def page_9(request, p1, p2, p3):
    return HttpResponse('p1 ' + p1 + ' p2 ' + p2 + ' p3 ' + p3)
url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
# 如果一个用户请求了URL “/articles/2005/05/39323/”，Django将调用函数news.views.article_detail(request, '2005', '05', '39323')。
```


## 无参数情况
```py
配置URL及其视图如下：
(r'^hello/$', hello)
 def hello(request):
    return HttpResponse("Hello World")
```
访问http://127.0.0.1:8000/hello，输出结果为“Hello World”


## 传递一个参数
配置URL及其视图如下,URL中通过正则指定一个参数：
```py
(r'^plist/(.+)/$', helloParam）
 def helloParam(request，param1):
    return HttpResponse("The param is : " + param1)
```
访问http://127.0.0.1:8000/plist/china，输出结果为”The param is : china”


## 传递多个参数
参照第二种情况，以传递两个参数为例，配置URL及其视图如下,URL中通过正则指定两个参数：
```py
(r'^plist/p1(\w+)p2(.+)/$', helloParams）
 def helloParams(request，param1,param2):
    return HttpResponse("p1 = " + param1 + "; p2 = " + param2)
```
访问http://127.0.0.1:8000/plist/p1chinap22012/
输出为”p1 = china; p2 = 2012″


## 通过传统的”?”传递参数
例如，http://127.0.0.1:8000/plist/?p1=china&p2=2012，url中‘?’之后表示传递的参数，这里传递了p1和p2两个参数。
通过这样的方式传递参数，就不会出现因为正则匹配错误而导致的问题了。在Django中，此类参数的解析是通过request.GET.get方法获取的。
```py
(r'^plist/$', hello）
 def hello(request):
    p1 = request.GET.get('p1')
    p2 = request.GET.get('p2')
    return HttpResponse("p1 = " + p1 + "; p2 = " + p2)
# 输出结果为”p1 = china; p2 = 2012″
```




## Django 2.0 使用 path 来代替 url
```py

```