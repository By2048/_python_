# 调用 google 翻译

## 安装
`pip install googletrans`


## 基础使用
```py

```


## 官方页面
[包介绍](http://py-googletrans.readthedocs.io/en/latest/)
[GitHub](https://github.com/ssut/py-googletrans)


## 示例代码
```py
from googletrans import Translator

translator = Translator(service_urls=['translate.google.cn'])

translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='zh-cn')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)

# The quick brown fox  ->  快速的棕色狐狸
# jumps over  ->  跳过
# the lazy dog  ->  懒惰的狗
```