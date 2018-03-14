import json
import requests
from collections import namedtuple

try:
    from config import *
except ImportError:
    from .config import *


def get_wallpaper_detail_link():
    pass


def get_category_list():
    category = namedtuple('category_info', ['id', 'name', 'count'])
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?' \
               'auth={0}&method=category_list'.format(api_code)

    html_data = requests.get(api_link)
    json_data = json.loads(html_data.text)

    categories = []
    for item in json_data['categories']:
        categories.append(category(item['id'], item['name'], item['count']))

    for item in categories:
        print(item.id, item.name, item.count, end='\n')


# get_category_list()


def get_img_in_category(category_id=1, page=1):
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?' \
               'auth={api_code}&method=category&id={category_id}&page={page}&info_level=3' \
                .format(api_code=api_code, category_id=category_id, page=page)
    print(api_link)
    html_data = requests.get(api_link)
    json_data = json.loads(html_data)
    print(json_data)


get_img_in_category()


def get_img_info(img_id):
    # img=namedtuple('img-info',['id',''])
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?' \
               'auth={0}&method=wallpaper_info&id={1}'.format(api_code, str(img_id))
    html_data = requests.get(api_link)
    json_data = json.loads(html_data.text)
    print(json_data)

    tags = []
    for item in json_data['tags']:
        tags.append(item['name'])

    id = json_data['wallpaper']['id']
    name = json_data['wallpaper']['name']
    file_type = json_data['wallpaper']['file_type']
    url = json_data['wallpaper']['url']

    category = json_data['wallpaper']['category']
    width = json_data['wallpaper']['width']
    height = json_data['wallpaper']['height']
    file_size = json_data['wallpaper']['file_size']

    return category, width, height, file_size, tags

# a, b, c, d, e = get_img_info(868745)
# print(a, b, c, d, e)
