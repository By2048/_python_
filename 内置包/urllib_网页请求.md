```py
import urllib.request

page_link = 'http://www.mzitu.com/all'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}

request = urllib.request.Request(page_link, headers=headers)
print(type(request))
print(request._full_url)
print(request)

html = urllib.request.urlopen(request)
print(html)
print(type(html))
print(html.read())

```

## 如何对url解码

```py
import urllib.parse
print(urllib.parse.unquote("%E6%B5%8B%E8%AF%95abc"))
```


```py
def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,*, cafile=None, capath=None, cadefault=False, context=None):
```