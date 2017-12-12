import urllib
import urllib.request
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
headers = {'User-Agent': user_agent}

start_page=r'https://share.dmhy.org/topics/list/page/1'

class dmhy:
    title = ""
    link = ""
    def __init__(self, title, link):
        self.title = title
        self.link = link


def get_down_link(link):
    html = urllib.request.Request(link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    for tr in soup.find('tbody').find_all('tr'):
        title=tr.find('td',class_='title').find('a',target='_blank').get_text()
        link=tr.find('td',nowrap='nowrap').find('a')['href']

        print(title)
        print(link)
        print('\n')

get_down_link(start_page)


