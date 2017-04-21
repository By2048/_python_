# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib.request, urllib.parse, urllib.error
import http.cookiejar


# user_agent ='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
# headers = { 'User-Agent' : user_agent ,'Connection': 'keep-alive'}

loginUrl="http://acm.usx.edu.cn/AspNet/"
infoUrl="http://acm.usx.edu.cn/AspNet/ShowUser.aspx?username=usx14305"
postData=urllib.parse.urlencode({
    "__EVENTTARGET":"",
    "__EVENTARGUMENT":"",
    "__VIEWSTATE":"/wEPDwULLTE0Njk0ODUxMjNkZDE3Terz2CiL41rmQXKBL7NjAtJo",
    "__VIEWSTATEGENERATOR":"EAE6C16D",
    "ctl00$LoginView$Login1$UserName":"usx14305",
    "ctl00$LoginView$Login1$Password":"cmeng",
    "ctl00$LoginView$Login1$LoginButton":"Login"
}).encode('utf-8')
headerData={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding":"utf-8",
    "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
    "Connection":"keep-alive",
    "Host":"acm.usx.edu.cn",
    "Referer":"http://acm.usx.edu.cn/AspNet/",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0"
}
infoData={
    "username":"usx14305"
}

def saveCookies(cookieJar):
    data=open('data.txt', 'w')
    for cj in cookieJar:
        data.writelines(cj.name)
        data.writelines('\n')
        data.writelines(cj.value)

request = urllib.request.Request(loginUrl,postData,headerData)

cookieJar = http.cookiejar.CookieJar()
httpCookieProcessor=urllib.request.HTTPCookieProcessor(cookieJar)
opener = urllib.request.build_opener(httpCookieProcessor)
response = opener.open(request)
# print(response.read().decode('utf-8'))
saveCookies(cookieJar)

info=urllib.request.Request(infoUrl,infoData,headerData)
print(info.decode('utf-8'))

