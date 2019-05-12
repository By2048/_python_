import sqlite3
import datetime
import time
import os
from bs4 import BeautifulSoup
import urllib
import urllib.request


has_down_path = os.path.abspath('has_down.txt')
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}

class meizi:
    link = ''
    title=''
    tag=''
    release_time=''
    browse_num = ''
    def __init__(self,  link,title,tag,release_time,browse_num):
        self.link = link
        self.title = title
        self.tag = tag
        self.release_time = release_time
        self.browse_num = browse_num

def init():
    if os.path.isfile('mzt-mmjpg.db'):
        pass
    else:
        cur.execute('''
        create table has_down
        (
            id              integer primary key autoincrement not null,
            link            varchar not null,
            title           nvarchar not null,
            tag             nvarchar not null,
            release_time    text not null,
            browse_num      integer not null
        );
        ''')


def keep_has_down_into_sql(info):
    item = [info.link, info.title, info.tag, info.release_time, info.browse_num]
    cur.execute("insert into has_down(link,title,tag,release_time,browse_num) values(?,?,?,?,?)", item)
    conn.commit()


# 获取已经下载的连接  has_down.txt -> has_down_list
def get_has_down():
    # file = open(has_down_path, 'r', encoding='utf-8')
    with open(has_down_path, 'r', encoding='utf-8') as file:
    # has_down = [line.strip() for line in file]
        has_down = [line.split('|')[1].strip() for line in file]
    return has_down



def get_other_info(link):
    html = urllib.request.Request(link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    infos = soup.find('div', class_='info').find_all('i')
    title=soup.find('div', class_='article').find('h2').get_text()
    time=infos[0].get_text()[5:]

    tags=soup.find('div', class_='tags')
    tag=','.join([item.get_text() for item in tags.find_all('a')])

    num=infos[3].get_text()[2:][1:-1]

    print(link+'    '+title+'   '+time+'   '+tag+'   '+num)

    return meizi(link,title,tag,time,num)

def insert_old_data():
    for url in get_has_down()[1:]:
        info=get_other_info(url)
        item=[info.link,info.title,info.tag,info.release_time,info.browse_num]
        cur.execute("insert into has_down(link,title,tag,release_time,browse_num) values(?,?,?,?,?)", item)
        conn.commit()


def get_has_down_by_sql():
    cur.execute("select * from has_down")
    cnt=0
    has_down_link=[]
    for item in cur.fetchall():
        # cnt+=1
        # item=[str(cnt),str(item[0]),item[1],item[2],item[3],item[4],str(item[5])]
        # print('    '.join(item))
        has_down_link.append(item[1])
    return has_down_link

if __name__ == '__main__':
    conn = sqlite3.connect('mzt-mmjpg.db')
    cur = conn.cursor()
    # insert_old_data()
    pp=get_has_down_by_sql()
    print('\n'.join(pp))
