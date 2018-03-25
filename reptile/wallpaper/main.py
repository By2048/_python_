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
    print('get_category_list'.ljust(25, ' ') + api_link)
    json_data = json.loads(requests.get(api_link).text)
    categories = []
    for item in json_data['categories']:
        categories.append(category(item['id'], item['name']))
    return categories


def get_category_img_count(category_id=1):
    api_link = "https://wall.alphacoders.com/api2.0/get.php?" \
               "auth={0}&method=category_count&id={1}".format(api_code, category_id)
    # print('get_category_img_count'.ljust(25, ' ') + api_link)
    json_data = json.loads(requests.get(api_link).text)
    return json_data['count']


def get_category_img(category_id=1, page=1):
    image = namedtuple('image_info', ['id', 'width', 'height', 'file_type', 'file_size',
                                      'url_image', 'url_thumb', 'url_page'])
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?' \
               'auth={0}&method=category&id={1}&page={2}&info_level=1'.format(api_code, category_id, page)
    print('get_category_img'.ljust(25, ' ') + api_link)
    json_data = json.loads(requests.get(api_link).text)
    images = []
    for item in json_data['wallpapers']:
        id = item['id']
        width = item['width']
        height = item['height']
        file_type = item['file_type']
        file_size = item['file_size']
        url_image = item['url_image']
        url_thumb = item['url_thumb']
        url_page = item['url_page']
        images.append(image(id, width, height, file_type, file_size, url_image, url_thumb, url_page))
        print(item)
    return images


def get_img_other_info(image_id):
    image = namedtuple('image_info', ['id', 'name', 'category', 'category_id', 'sub_category', 'sub_category_id',
                                      'user_name', 'user_id', 'tags'])
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?' \
               'auth={0}&method=wallpaper_info&id={1}'.format(api_code, str(image_id))
    print('get_img_other_info'.ljust(25, ' ') + api_link)
    json_data = json.loads(requests.get(api_link).text)
    id = str(image_id)

    if json_data['wallpaper']['name'] != None:
        name = json_data['wallpaper']['name']
    else:
        name = ''
    category = json_data['wallpaper']['category']
    category_id = json_data['wallpaper']['category_id']
    sub_category = json_data['wallpaper']['sub_category']
    sub_category_id = json_data['wallpaper']['sub_category_id']
    user_name = json_data['wallpaper']['user_name']
    user_id = json_data['wallpaper']['user_id']
    tags = json_data['tags']

    image = image(id, name, category, category_id, sub_category, sub_category_id, user_name, user_id, tags)
    return image


def get_api_count():
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?auth={0}&method=query_count'.format(api_code)
    json_data = json.loads(requests.get(api_link).text)
    json_info = json.dumps(json_data, sort_keys=False, indent=4)
    print(json_info)


def start():
    for category_id in range(1, 34):
        img_count = get_category_img_count(category_id)
        if int(img_count) < 500:
            max_page = 300 // 30
        elif int(img_count) < 1000:
            max_page = 700 // 30
        else:
            max_page = 101

        for page_num in range(1, max_page):
            images = get_category_img(category_id, page_num)
            insert_base_info(images)

            # 获取详细信息
            # for image in images:
            #     image_info = get_img_other_info(image.image_id)
            #     insert_other_info(image_info)


def _test():
    for i in range(1, 12):
        print(i)
    for i in range(12, 34):
        print(i)


if __name__ == '__main__':
    all_categorie = get_category_list()
    insert_category(all_categorie)

    # 获取每个分类下图片的数量
    # for item in all_categorie:
    #     img_num = get_category_img_count(item[0])
    #     print('{:<3}   {:<15}   {:<10}'.format(item[0], item[1], str(img_num)))

    images = get_category_img()
    insert_base_info(images)

    for image_id in get_image_id():
        image_info = get_img_other_info(int(image_id))
        insert_other_info(image_info)
