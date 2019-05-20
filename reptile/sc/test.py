import requests
from bs4 import BeautifulSoup

# data = requests.get('https://chan.sankakucomplex.com/?tags=fav%3AAM153&page=1')
# response = requests.get('https://chan.sankakucomplex.com/post/show/4586463')
#
# soup = BeautifulSoup(response.content)
#
# image = soup.find(id='image-link')
#
# print(image)

import shutil

import requests

# soup.find(id='image-link').find('img')['src'].lstrip('//')

url = 'http://cs.sankakucomplex.com/data/6d/6a/6d6aa5d38fa002f29a6cc52287fca0e7.png?e=1558377975&m=qxcMdUvUiuddO79vtPgNWw'
response = requests.get(url, stream=True)
with open('img.png', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response