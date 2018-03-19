import requests
import os, re


def get_all_img_id():
    test_link = 'http://101.132.185.153:2199/'
    response = requests.get(test_link, auth=('user_admin', 'qwer1234'))
    re_rule = '(?<=<a href=")(\d+?)(?=/">)'
    img_ids = (re.findall(re_rule, response.text))
    return img_ids


def get_img_link(img_id=100005):
    index_link = 'http://101.132.185.153:2199/'
    test_link = index_link + str(img_id)
    response = requests.get(test_link, auth=('user_admin', 'qwer1234'))
    re_rule = '(?<=<a href=")(\w+?\.\w+?)(?=">)'
    img_names = (re.findall(re_rule, response.text))
    img_links = []
    for img_name in img_names:
        img_links.append(test_link + '/' + img_name)
    return img_links


get_img_link()
