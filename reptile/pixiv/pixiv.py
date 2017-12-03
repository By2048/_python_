# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import urllib.request
import multiprocessing
import time
import re
import random
import sys
import urllib

class Img:
    link = ""
    name = ""
    alt = ''
    def __init__(self, link, name, alt):
        self.link = link
        self.name = name
        self.alt = alt

login_header = {
    'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
login_params = {
    'lang': 'zh',
    'source': 'pc',
    'view_type': 'page',
    'ref': 'wwwtop_accounts_index'
}
login_data = {
    'pixiv_id': '2045516477@qq.com',
    'password': 'dojopv12',
    'captcha': '',
    'g_recaptcha_response': '',
    'post_key': '',
    'source': 'pc',
    'ref': 'wwwtop_accounts_index',
    'return_to': 'http://www.pixiv.net/'
}
pixiv_path = "F:\\Image\\pixiv\\"
login_session = requests.Session()
login_session.headers = login_header


def get_post_key():
    login_key_html = login_session.get(url='https://accounts.pixiv.net/login', params=login_params)
    pattern = re.compile(r'name="post_key" value="(.*?)">')
    post_key = pattern.findall(login_key_html.text)[0]
    return post_key

def login():
    login_data['post_key'] = get_post_key()
    login_session.post(url='https://accounts.pixiv.net/api/login?lang=zh', data=login_data)

def create_keep_path(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def get_pages_num(user_id):
    user_index_link = 'http://www.pixiv.net/member_illust.php?id=' + user_id
    html = login_session.get(user_index_link, headers=login_header)
    soup = BeautifulSoup(html.text, 'html.parser')
    for li in soup.find('ul', attrs={'class', 'page-list'}):
        num = li.get_text()
    return num

def get_img_in_page(user_id, page_num):
    index_link = 'http://www.pixiv.net/member_illust.php?id={user_id}&type=all&p={page}' \
        .format(user_id=user_id, page=page_num)
    img_links = []
    html = login_session.get(index_link, headers=login_header)
    soup = BeautifulSoup(html.text, 'html.parser')
    ul = soup.find('ul', attrs={'class', '_image-items'})
    for li in ul.find_all('li', attrs={'class', 'image-test-item'}):
        # img_link_1 = li.find('a', attrs={'class', 'work _work '})['href']
        # img_link_2 = li.find('a', attrs={'class', 'work  _work multiple '})['href']
        img_link = li.find('a')['href']
        img_links.append('http://www.pixiv.net' + img_link)
    return img_links

def get_one_detail_img(link):
    html = login_session.get(link, headers=login_header)
    soup = BeautifulSoup(html.text, 'html.parser')
    div = soup.find('div', attrs={'class', '_illust_modal _hidden ui-modal-close-box'})
    try:
        image = div.find('img', attrs={'class', 'original-image-test'})
        img_link = image['data-src']
        img_alt = image['alt']
        img_name = img_link.split('/')[-1]
        img = Img(link=img_link, name=img_name, alt=img_alt)
    except:
        pass
    return img

def get_more_detail_img(link):
    link=link.replace('medium','manga')
    imgs = []
    html = login_session.get(link, headers=login_header)
    soup = BeautifulSoup(html.text, 'html.parser')
    all_div = soup.find('section', attrs={'class', 'manga'})
    for img_div in all_div:
        try:
            for img in img_div.find_all('img', attrs={'class', 'image-test ui-scroll-view'}):
                img_link = img['data-src']
                img_name = img_link.split('/')[-1]
                img_alt = ''
                imgs.append(Img(link=img_link, name=img_name, alt=img_alt))
        except:
            pass
    return imgs

def get_detail_img(link, img_num):
    imgs = []
    if img_num == '1':
        html = login_session.get(link, headers=login_header)
        soup = BeautifulSoup(html.text, 'html.parser')
        div = soup.find('div', attrs={'class', '_illust_modal _hidden ui-modal-close-box'})
        try:
            iamge = div.find('img', attrs={'class', 'original-image-test'})
            img_link = iamge['data-src']
            img_alt = iamge['alt']
            img_name = img_link.split('/')[-1]
            imgs.append(Img(link=img_link, name=img_name, alt=img_alt))
        except:
            pass
    else:
        html = login_session.get(link, headers=login_header)
        soup = BeautifulSoup(html.text, 'html.parser')
        all_div = soup.find('section', attrs={'class', 'manga'})
        for img_div in all_div:
            try:
                for img in img_div.find_all('img', attrs={'class', 'image-test ui-scroll-view'}):
                    img_link = img['data-src']
                    img_name = img_link.split('/')[-1]
                    img_alt = ''
                    imgs.append(Img(link=img_link, name=img_name, alt=img_alt))
            except:
                pass
    return imgs

def one_or_many(link):
    html = login_session.get(link, headers=login_header)
    soup=BeautifulSoup(html.text, 'html.parser')
    div=soup.find('div',attrs={'class','multiple'})
    if div==None:
        return 'one'
    else:
        return 'many'

def download_image(img,folder_path):
    try:
        print('Download... ' + img.link)
        html = requests.get(img.link, headers=login_header)
        image = html.content
        with open(folder_path + img.name, 'ab') as file:
            file.write(image)
    except:
        print('Download fail')

def get_user_name(user_id):
    user_index='http://www.pixiv.net/member.php?id={id}'.format(id=user_id)
    html=login_session.get(user_index,headers=login_header)
    soup=BeautifulSoup(html.text,'html.parser')
    user_name =soup.find('h1',class_='user').get_text()
    user_name=user_name.replace('//','')
    return user_name

if __name__ == '__main__':
    user_id='17990799'
    login()
    user_name=get_user_name(user_id)
    folder_path=pixiv_path+ user_name+'_'+user_id+'\\'
    create_keep_path(folder_path)
    max_pages_num = get_pages_num(user_id)
    for num in range(int(max_pages_num)):
        images = get_img_in_page(user_id, str(num+1))
        for link in images:
            if one_or_many(link)=='one':
                tmp = get_one_detail_img(link)
                download_image(tmp,folder_path)
            else:
                imgs=get_more_detail_img(link)
                for tmp in imgs:
                    download_image(tmp,folder_path)
            time.sleep(3)

