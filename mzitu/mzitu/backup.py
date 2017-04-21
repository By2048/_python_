# Coding=utf-8
# Author By2048 Time 2017-1-18
import os
import urllib
import urllib.request
from bs4 import BeautifulSoup
import multiprocessing
import re
import socket


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


