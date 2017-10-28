import requests
import time


# data=requests.get(link,allow_redirects=True)

# headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#            'Accept-Encoding': 'gzip, deflate, compress',
#            'Accept-Language': 'en-us;q=0.5,en;q=0.3',
#            'Cache-Control': 'max-age=0',
#            'Connection': 'keep-alive',
#            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

headers={'Host': 'img.mmjpg.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Accept': '*//*',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.mmjpg.com/mm/1087',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'}




for i in range(1,46):
    link='http://img.mmjpg.com/2017//1087/'+str(i)+'.jpg'
    path='F:\\- Test\\'+str(i)+'.jpg'


    data=requests.get(link,headers=headers)

    with open (path,'wb') as file:
        file.write(data.content)
    time.sleep(3)



