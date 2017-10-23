from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
from urllib import parse

from image import *

str_lk='''%E6%8E%A8%E8%8D%90'''
print(parse.quote('推荐'))

print (sys.getdefaultencoding())

print(u'%E6%8E%A8%E8%8D%90'.encode('gb2312'))

print(parse.unquote(str_lk))

print(parse.unquote_plus('1+2'))
print(parse.unquote('1+2'))

url = r'https://docs.python.org/3.5/search.html?q=parse&check_keywords=yes&area=default'
print(parse.urlparse(url))
param_dict = parse.parse_qs(parse.urlparse(url).query)
print(param_dict)
print(param_dict['q'][0])
print(parse.parse_qs('proxy=183.222.102.178:8080&task=XXXXX|5-3+2'))
print(parse.parse_qs('action=addblog&job=modify&tid=1766670'))
print(parse.parse_qsl('action=addblog&job=modify&tid=1766670'))

s = 'id%253D184ff84d27c3613d%26quality%3Dmedium'
print(parse.unquote(parse.unquote(s)))
print(parse.unquote(s))


query = {
    'name': 'walker',
    'age': 99,
    }
print(parse.urlencode(query))


print(parse.quote('a&b/c'))
print(parse.quote_plus('a&b/c'))


pp=bili_img('1','name','author','down_link','10','upload_time','tag','md5','charcater_name','source_anime','description')

pp.print()