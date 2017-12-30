# # Coding=utf-8
# # Author By2048 Time 2017-1-18
# import os
# import urllib
# import urllib.request
# from bs4 import BeautifulSoup
# import multiprocessing
# import re
# import socket


start_url = 'http://www.mzitu.com/all'
# 获取主页下所有的meizi连接
def get_all_link(start_url):
    all_meizi_link = []
    html = urllib.request.Request(start_url, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    all_ul = soup.find_all('ul', class_='archives')
    for ul in all_ul:
        links = ul.find_all('a')
        for link in links:
            tmp = meizi(change_coding(link.get_text()), link['href'])
            all_meizi_link.append(tmp)
    return all_meizi_link



# 获取已经下载的图片链接
def get_has_down_by_txt():
    file = open(has_down_txt_path, 'r', encoding='utf-8')
    has_down = [line.split('<|>')[0].strip() for line in file]
    return has_down


# 保存已经下载的链接到
def keep_has_down_to_txt(meizi):
    has_down_txt = open(has_down_txt_path, 'a', encoding='utf-8')
    split_text = '\t' + '<|>' + '\t'
    has_down_txt.write(
        meizi.link + split_text +
        meizi.title + split_text +
        meizi.category + split_text +
        meizi.date + '\n')
    has_down_txt.close()

"""
CREATE TABLE has_down
(
  id         INTEGER PRIMARY KEY,
  link       TEXT     NOT NULL,
  title      TEXT     NOT NULL,
  category   TEXT     NOT NULL,
  date       TEXT     NOT NULL
);
select * from has_down
delete from has_down
SELECT link FROM has_down
"""
