import json
import requests
from collections import namedtuple

try:
    from .sql import *
except ImportError:
    from sql import *

api_code = 'cbf61fb8197d5fdc054041c1bd2945e9'


def get_category_list():
    category = namedtuple('category_info', ['id', 'name'])
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?' \
               'auth={0}&method=category_list'.format(api_code)
    json_data = json.loads(requests.get(api_link).text)
    categories = []
    for item in json_data['categories']:
        categories.append(category(item['id'], item['name']))
    return categories



def get_category_img_count(category_id=1):
    api_link="https://wall.alphacoders.com/api2.0/get.php?" \
             "auth={0}&method=category_count&id={1}".format(api_code,category_id)
    json_data = json.loads(requests.get(api_link).text)
    print(json_data['count'])

def get_img_in_category(category_id=1, page=1):
    image = namedtuple('image_info', ['image_id', 'category_id', 'image_url', 'image_url_thumb'])
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?' \
               'auth={0}&method=category&id={1}&page={2}&info_level=3'.format(api_code, category_id, page)
    json_data = json.loads(requests.get(api_link).text)
    images = []
    for item in json_data['wallpapers']:
        image_id = item['id']
        category_id = item['category_id']
        image_url = item['url_image']
        image_url_thumb = item['url_thumb']
        images.append(image(image_id, category_id, image_url, image_url_thumb))
    return images


def get_img_other_info(image_id):
    image = namedtuple('img_info', ['image_id', 'name', 'width', 'height', 'file_type', 'file_size', 'tags'])
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?' \
               'auth={0}&method=wallpaper_info&id={1}'.format(api_code, str(image_id))
    json_data = json.loads(requests.get(api_link).text)
    name = json_data['wallpaper']['name']
    width = json_data['wallpaper']['width']
    height = json_data['wallpaper']['height']
    file_type = json_data['wallpaper']['file_type']
    file_size = json_data['wallpaper']['file_size']
    tags = json_data['tags']
    return image(image_id, name, width, height, file_type, file_size, tags)


def get_api_count():
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?auth={0}&method=query_count'.format(api_code)
    json_data = json.loads(requests.get(api_link).text)
    print(json_data)


def _test_get():
    category_list = get_category_list()
    for item in category_list:
        print(item.id, item.name)

    images = get_img_in_category(category_id=1, page=1)
    for item in images:
        print(item.image_id, item.category_id, item.image_url, item.image_url_thumb)

    image_info = get_img_other_info(885581)
    print(image_info.name, image_info.width, image_info.height,
          image_info.file_type, image_info.file_size, image_info.tags)
    print(type(image_info.tags))
    print([item['id'] for item in image_info.tags])
    tag_id = ','.join([item['id'] for item in image_info.tags])
    print(tag_id)

def start():
    categories = get_category_list()
    insert_category(categories)

    for category_id in range(1, 34):
        for page_num in range(1, 101):
            images = get_img_in_category(category_id, page_num)
            insert_base_info(images)
            # 获取详细信息
            # for image in images:
            #     image_info = get_img_other_info(image.image_id)
            #     insert_other_info(image_info)


def _test():
    for i in range(1,12):
        print(i)
    for i in range(12,34):
        print(i)


if __name__ == '__main__':
    categories = get_category_list()
    insert_category(categories)
