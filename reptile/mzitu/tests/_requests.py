import requests
import time
from bs4 import BeautifulSoup
import urllib.request


all_img_page_link = 'http://www.mzitu.com/all'

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}




html_text=requests.get(all_img_page_link,headers=headers).text
soup = BeautifulSoup(html_text, "html.parser")
print(soup)

