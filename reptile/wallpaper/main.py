import urllib
import urllib.request
from urllib import parse
import sys

from bs4 import BeautifulSoup

try:
    from config import *
except ImportError:
    from .config import *


def get_index_info(link):
    html = urllib.request.Request(link, headers=headers)
    request = urllib.request.urlopen(html)
    soup = BeautifulSoup(request, "html.parser")
    print(soup)


# API key: cbf61fb8197d5fdc054041c1bd2945e9

# get_index_info(index_link)

category_link_1 = get_category_link(1)
print(category_link_1)


def get_wallpaper_detail_link():
    pass