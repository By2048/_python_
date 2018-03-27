import json
import sqlite3
import requests
from collections import namedtuple
import multiprocessing
from collections import deque
import os

api_code = 'cbf61fb8197d5fdc054041c1bd2945e9'

sql_path = 'T:\\_tmp\\image.db'

# sql_path = '/home/python/wallpaper/image.db'


class image_base_info(object):
    """图片的基础信息
    Attributes:
        id
        width
        height
        file_type
        file_size
        url_image   图片的链接
        url_thumb   缩略图的链接
        url_page    对应的页面
    """

    def __init__(self, id, width, height, file_type, file_size, url_image, url_thumb, url_page):
        self.id = id
        self.width = width
        self.height = height
        self.file_type = file_type
        self.file_size = file_size
        self.url_image = url_image
        self.url_thumb = url_thumb
        self.url_page = url_page


class image_other_info(object):
    """图片的其他信息
    Attributes:
        id
        name
        category
        category_id
        sub_category
        sub_category_id
        user_name
        user_id
        tags                图片的标签 str类型  [{'id': '2578', 'name': 'swirl'}, {'id': '463', 'name': 'purple'}]
    """

    def __init__(self, id, name, category, category_id, sub_category, sub_category_id, user_name, user_id, tags):
        self.id = id
        self.name = name
        self.category = category
        self.category_id = category_id
        self.sub_category = sub_category
        self.sub_category_id = sub_category_id
        self.user_name = user_name
        self.user_id = user_id
        self.tags = tags

    def __str__(self):
        return "{0:<9} {1:<15} {2:<3} {3:<15} {4}".format(self.id, repr(self.name), self.category_id, self.category,
                                                          self.tags)


def get_image_id() -> list:
    """
    获取数据库中所有未添加图片具体信息的图片的ID  即 tags=''
    :return:
        所有未添加具体信息图片的ID
    """
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    cur.execute("SELECT * FROM image WHERE tags = ''")
    all_image_id = [item[0] for item in cur.fetchall()]
    return all_image_id


def init_sql():
    """
    初始化 image.db 数据库
    :return:
    """
    if os.path.isfile(sql_path):
        os.remove(sql_path)

    create_category = """create table category
    (
        id     text,
        name   text
    );"""

    create_image = """create table image
    (
        id              text,
        width           text,
        height          text,
        file_type       text,
        file_size       text,
        url_image       text,
        url_thumb       text,
        url_page        text,
        name            text,
        category        text,
        category_id     text,
        sub_category    text,
        sub_category_id text,
        user_name       text,
        user_id         text,      
        tags            text      
    );"""

    create_tag = """create table tag
    (
        id      text,
        name    text
    );"""

    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    cur.execute(create_category)
    cur.execute(create_image)
    cur.execute(create_tag)
    con.commit()
    con.close()


def insert_category(categorys: namedtuple):
    """
    category 插入到数据库
    :param categorys:

    :return:
    """
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    for item in categorys:
        insert_sql = "insert into category(id,name) values('{id}','{name}')" \
            .format(id=item.id, name=item.name)
        cur.execute(insert_sql)
        print(insert_sql)
    con.commit()
    con.close()


def insert_tag(tags: str):
    """
    tags 插入到数据库
    :param tags :
    :return:
    """

    tags = json.loads(tags)
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    for tag in tags:
        insert_sql = "insert into tag(id,name) " \
                     "select '{id}','{name}' " \
                     "where not exists (select id from tag where id='{id}')" \
            .format(id=tag['id'], name=tag['name'])
        cur.execute(insert_sql)
        print(insert_sql)
    con.commit()
    con.close()


def update_other_info(images: list):
    """
    图片的其他信息插入到数据库
    :param image lsit:
    :return:
    """
    con = sqlite3.connect(sql_path)
    cur = con.cursor()
    for image in images:
        update_sql = "update image " \
                     "set name='{0}',category='{1}',category_id='{2}',sub_category='{3}',sub_category_id='{4}',user_name='{5}',user_id='{6}',tags=\"{7}\" " \
                     "where id='{8}'".format(image.name, image.category, image.category_id, image.sub_category,
                                             image.sub_category_id, image.user_name, image.user_id, image.tags,
                                             image.id)
        print(update_sql)
        cur.execute(update_sql)
    con.commit()
    con.close()


def get_category_list() -> list:
    """
    获取所有的分类
    :return:
        所有的分类
    """
    category = namedtuple('category_info', ['id', 'name'])
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?' \
               'auth={0}&method=category_list'.format(api_code)
    print('get_category_list'.ljust(25, ' ') + api_link)
    json_data = json.loads(requests.get(api_link).text)
    categories = []
    for item in json_data['categories']:
        categories.append(category(item['id'], item['name']))
    return categories


def get_category_img_count(category_id: int) -> int:
    """
    获取一个分类下图片的总数
    :param category_id:
    :return:
        分类下图片的数量
    """
    api_link = "https://wall.alphacoders.com/api2.0/get.php?" \
               "auth={0}&method=category_count&id={1}".format(api_code, category_id)
    # print('get_category_img_count'.ljust(25, ' ') + api_link)
    json_data = json.loads(requests.get(api_link).text)
    return int(json_data['count'])


def get_all_category_image_count():
    """
    获取每个分类下图片的数量
    """
    all_categorie = get_category_list()
    for item in all_categorie:
        img_num = get_category_img_count(item[0])
        print('{:<3}   {:<15}   {:<10}'.format(item[0], item[1], str(img_num)))


def get_category_img(category_id: int, page: int) -> list:
    """
    获取分类下某一页所有图片的基础信息
    :param category_id:分类的ID
    :param page: 页数
    :return: 图片的基础信息
    """

    api_link = 'https://wall.alphacoders.com/api2.0/get.php?' \
               'auth={0}&method=category&id={1}&page={2}&info_level=1'.format(api_code, category_id, page)
    print('get_category_img'.ljust(25, ' ') + api_link)
    json_data = json.loads(requests.get(api_link).text)

    all_image = []
    for item in json_data['wallpapers']:
        id = item['id']
        width = item['width']
        height = item['height']
        file_type = item['file_type']
        file_size = item['file_size']
        url_image = item['url_image']
        url_thumb = item['url_thumb']
        url_page = item['url_page']
        all_image.append(image_base_info(id, width, height, file_type, file_size, url_image, url_thumb, url_page))
    return all_image


def get_img_other_info(image_id: int) -> image_other_info:
    """
    获取图片的其他信息
    :param image_id:图片的ID
    :return: 图片的其他信息
    """
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?' \
               'auth={0}&method=wallpaper_info&id={1}'.format(api_code, str(image_id))
    print('get_img_other_info'.ljust(25, ' ') + api_link)
    json_data = json.loads(requests.get(api_link).text)

    id = str(image_id)
    name = json_data['wallpaper']['name']
    category = json_data['wallpaper']['category']
    category_id = json_data['wallpaper']['category_id']
    sub_category = json_data['wallpaper']['sub_category']
    sub_category_id = json_data['wallpaper']['sub_category_id']
    user_name = json_data['wallpaper']['user_name']
    user_id = json_data['wallpaper']['user_id']
    tags = str(json_data['tags'])

    # name = '' if name == None else name
    # category = '' if category == '' else category
    # category_id = '0' if category_id == '' else category_id
    # category_id = '0' if category_id == '' else category_id
    # sub_category = '' if sub_category == '' else sub_category
    # sub_category_id = '0' if sub_category_id == '' else sub_category_id
    # user_name = '' if user_name == '' else user_name
    # user_id = '0' if user_id == '' else user_id
    # tags = '' if tags == '' else tags

    return image_other_info(id, name, category, category_id, sub_category, sub_category_id, user_name, user_id, tags)


def get_api_count() -> json:
    """获取API使用的次数
    :return
        返回请求后格式化的Json数据 如下
        {
            "counts": {
                "month_price": 0,
                "month_count": 18362,
                "last_month_count": 0,
                "last_month_price": 0
            },
            "success": true
        }
    """
    api_link = 'https://wall.alphacoders.com/api2.0/get.php?auth={0}&method=query_count'.format(api_code)
    json_data = json.loads(requests.get(api_link).text)
    json_info = json.dumps(json_data, sort_keys=False, indent=4)
    print(json_info)


def init_image_base_info():
    """
    获取图片的基础信息
    :return:
    """
    con = sqlite3.connect(sql_path)
    cur = con.cursor()

    for category_id in range(1, 34):
        img_count = get_category_img_count(category_id)

        if int(img_count / 1000 * 20) > 100:
            max_page = 100
        else:
            max_page = int(img_count / 1000 * 20)

        pool = multiprocessing.Pool(processes=max_page + 1)

        return_image = []
        for page_num in range(1, max_page):
            # process = multiprocessing.Process(target=get_category_img, args=(category_id, page_num,))
            # process.start()
            return_image.append(pool.apply_async(get_category_img, (category_id, page_num,)))
        pool.close()
        pool.join()

        insert_list = []
        for images in return_image:
            for img in images.get():
                insert_list.append((img.id, img.width, img.height, img.file_type, img.file_size, img.url_image,
                                    img.url_thumb, img.url_page, '', '', '', '', '', '', '', ''))
        cur.executemany('INSERT INTO image VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', insert_list)
    con.commit()
    con.close()


def init_image_other_info():
    """
    在获取图片基础信息的基础上获取图片的其他信息
    :return:
    """

    all_image_id = get_image_id()

    max_pool_num = multiprocessing.cpu_count()
    for i in range(0, len(all_image_id), max_pool_num):
        pool = multiprocessing.Pool(processes=max_pool_num)
        return_image = []
        image_ids = all_image_id[i:i + max_pool_num]
        for image_id in image_ids:
            return_image.append(pool.apply_async(get_img_other_info, (image_id,)))
        pool.close()
        pool.join()
        update_list = []
        for image in return_image:
            img = image.get()
            update_list.append(img)
        update_other_info(update_list)
        # cur.executemany(
        #     "UPDATE image SET name=?,category=?,category_id=?,sub_category=?,sub_category_id=?,"
        #     "user_name=?,user_id=?,tags=? WHERE id=?", insert_list)


def init_category():
    """
    数据库初始化分类
    :return:
    """
    all_categorie = get_category_list()
    insert_category(all_categorie)


if __name__ == '__main__':
    get_api_count()
    # init_image_base_info()
    init_image_other_info()
