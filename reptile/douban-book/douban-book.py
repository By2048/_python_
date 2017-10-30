#code=utf-8
from bs4 import BeautifulSoup
import re
import urllib
import urllib.request
import urllib.error
import multiprocessing
import time
from openpyxl import Workbook
from openpyxl import load_workbook

tag=["小说","随笔","散文","诗歌","童话","名著","历史","哲学","科普"]

# 图书信息结构
class Book:
    name=""
    author=""
    img_url=""  # 图书图片连接地址
    book_url=""
    press=""   #出版社
    publication_year=""    #出版日期
    pages_num=""   #页数
    price=""
    ISBN=""
    point=""
    rating_people = ""  # 评价的人数
    book_introduction=""   #图书介绍
    author_introduction="" #作者介绍
    def __init__(self,name,author,img_url,book_url,press,publication_year,pages_num,price,ISBN,point,rating_people,book_introduction,author_introduction):
        self.name = name
        self.author = author
        self.img_url = img_url
        self.book_url = book_url
        self.press = press
        self.publication_year = publication_year
        self.pages_num = pages_num
        self.price = price
        self.ISBN = ISBN
        self.point = point
        self.rating_people = rating_people
        self.book_introduction = book_introduction
        self.author_introduction = author_introduction


user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = { 'User-Agent' : user_agent }

tag=["小说","随笔","散文","诗歌","童话","名著","历史","哲学","科普"]
# https://book.douban.com/tag/
# urlStart="https://book.douban.com/tag/"     # https://book.douban.com/tag/小说?start=20
urlStart = "https://book.douban.com/top250?start="


first_url_list=[]
book_info_list=[]

# 输出信息 name author price point author_introduction book_introduction
def printInfo(book):
    print ('Name: {0}   Author: {1}   Price: {2}   Point: {3}'.format(book.name,book.author,book.price,book.point))
    print('Author_Introduction: '+book.author_introduction)
    print('Book_Introduction: ' + book.book_introduction)

def bookInfoToList(book):
    list=[book.name,
          book.author,
          book.publication_year,
          book.pages_num,
          book.price,
          book.ISBN,
          book.point,
          book.rating_people,
          book.press,
          book.img_url,
          book.book_url,
          book.book_introduction,
          book.author_introduction]
    return list

def keepBookData(book):
    fill = open('BooksInfo.txt', 'a')
    fill.write(book.name+'\n'+
               book.author+'\n'+
               book.publication_year+'\n'+
               book.pages_num+'\n'+
               book.price+'\n'+
               book.ISBN+'\n'+
               book.point+'\n'+
               book.rating_people+'\n'+
               book.press + '\n' +
               book.img_url + '\n' +
               book.book_url + '\n' +
               book.book_introduction+'\n'+
               book.author_introduction)
    fill.write('\n'+'-----------------------------------------------'+'\n\n\n')

def keepSqlData(book):
    fill = open('sql_data.txt', 'a')

def get_first_url():
    for i in range(11):
        request=urllib.request.urlopen(urlStart+str(i*25))
        soup=BeautifulSoup(request,"html.parser")
        links=soup.find_all('a',class_="nbg")
        for tmp in links:
            first_url_list.append(tmp['href'])

def CG(data):
    data=data.replace(' ', '')
    data = data.replace(':', '')
    data=data.replace('元', '')
    return data

def get_book_info(book_url):
    book_info=Book(None,None,None,None,None,None,None,None,None,None,None,None,None)
    html = urllib.request.Request(book_url,headers=headers)
    request=urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")

    name=soup.find('h1').find('span').get_text()
    img_url=soup.find('div',id='mainpic').find('img')['src']
    point=soup.find('strong').string
    point=CG(point)
    rating_people=soup.find('a',class_='rating_people').get_text()
    rating_people=rating_people[0:-3]

    book_info.book_url=book_url
    book_info.name = name
    book_info.img_url = img_url
    book_info.point=point
    book_info.rating_people=rating_people

    for tmp in soup.find('div',id='info').find_all('span'):
        if(CG(tmp.get_text())=='作者'):
            author=tmp.next_sibling.next_sibling.get_text()
            book_info.author=author
        if (CG(tmp.get_text()) == '出版社'):
            press=tmp.next_sibling
            book_info.press=CG(press)
        if (CG(tmp.get_text()) == '出版年'):
            publication_year=tmp.next_sibling
            book_info.publication_year=CG(publication_year)
        if (CG(tmp.get_text()) == '页数'):
            pages_num = tmp.next_sibling
            book_info.pages_num=CG(pages_num)
        if (CG(tmp.get_text()) == '定价'):
            price = CG(tmp.next_sibling)
            book_info.price=price
        if (CG(tmp.get_text()) == 'ISBN'):
            ISBN = tmp.next_sibling
            book_info.ISBN=CG(ISBN)

    author_introduction=''
    book_introduction=''

    tmp_count=0
    introduction=soup.find_all('div',class_='intro')
    try:
        pd=False
        info=introduction[tmp_count].find_all('p')

        # Count == 0    ???
        for i in info:
            if not (i.find('a')) is None:
                pd=True
                tmp_count+=1
        if(pd==False):
            info = introduction[tmp_count].find_all('p')
            for i in info:
                book_introduction+=str(i)
        else:
            info = introduction[tmp_count].find_all('p')
            for i in info:
                book_introduction += str(i)
    except:
        print('Error_1 {0}'.format(book_url))
    finally:
        tmp_count+=1
        book_info.book_introduction=book_introduction

    try:
        pd=False
        info=introduction[tmp_count].find_all('p')
        for i in info:
            if not (i.find('a')) is None:
                tmp_count+=1
                pd=True
        if (pd == False):
            info = introduction[tmp_count].find_all('p')
            for i in info:
                author_introduction += str(i)
        else:
            info = introduction[tmp_count].find_all('p')
            for i in info:
                author_introduction += str(i)
    except:
        print('Error_2 {0}'.format(book_url))
        author_introduction='No Author Introduction'
    finally:
        book_info.author_introduction=author_introduction
    book_info_list.append(book_info)
    return book_info

if __name__ == '__main__':
    get_first_url()
    for url in first_url_list:
        try:
            book=get_book_info(url)
            keepBookData(book)
            printInfo(book)
        except:
            print('Error_3 {0}'.format(url))









