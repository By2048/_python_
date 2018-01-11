# Coding=utf-8
# Author By2048 Time 2017-1-18

from bs4 import BeautifulSoup
import requests

try:
    from .color_print import *
    from .config import *
    from .sql import *
    from .downloads import *
    from .tools import *
    from .items import *
except ImportError:
    from color_print import *
    from config import *
    from sql import *
    from downloads import *
    from tools import *
    from items import *


# 获取一个页面的最大图片数量 方便合成连接
def get_image_num(soup):
    max_num = 0
    for span in soup.find('div', class_='pagenavi').find_all('span'):
        if (span.get_text() == '下一页»'):
            max_num = span.parent.previous_sibling.find('span').get_text()
    return int(max_num)


# 获取第一张图片下载的连接
def get_first_img_down_link(soup):
    img_down_link = ''
    try:
        img = soup.find('div', class_='main-image').find('img')
        img_down_link = img['src']
    except:
        print('Get_img_link_fail')
    finally:
        return img_down_link


# 获取图片的 分类 日期
def get_categroy_date(soup):
    all_span = soup.find('div', class_='main-meta').find_all('span')
    category = all_span[0].find('a').get_text()
    date = all_span[1].get_text().replace('发布于 ', '')
    return category, date


# 获取图片的其他信息
def get_other_info(detail_link):
    html=requests.get(detail_link,headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    max_num = get_image_num(soup)
    first_down_link = get_first_img_down_link(soup)
    category, date = get_categroy_date(soup)
    return max_num, first_down_link, category, date


#  获取第一张图片的下载地址 根据下载地址合成其他下载连接
def get_down_link_list_by_str(first_down_link, max_num):
    """
    http://i.meizitu.net/2017/10/29c02.jpg
    start_link   http://i.meizitu.net/2017/10
    image_name   29c02.jpg
    _str    29c
    _num    02
    _type   jpg
    """
    start_link, image_name = os.path.split(first_down_link)
    _str = image_name.split('.')[0][:-2]
    _num = int(image_name.split('.')[0][-2:])
    _type = image_name.split('.')[1]

    down_link_list = []
    for num in range(_num, _num + max_num):
        down_link_list.append(start_link + '/' + _str + str(num).zfill(2) + '.' + _type)
    return down_link_list


# 获取 all_img_page 下所有的信息 title link
def get_all_meizi():
    html=requests.get(all_img_page_link,headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")

    all_meizi = []
    for ul in soup.find_all('ul', class_='archives'):
        for link in ul.find_all('a'):
            # 进行编码转换
            # mz = Meizi(change_coding(link.get_text()), link['href'], '', '')
            mz = Meizi(link['href'].split('/')[-1], link.get_text(), link['href'], '', '')
            all_meizi.append(mz)
    return all_meizi


# 获取主页的页数
def get_page_max_num():
    html=requests.get(start_page_link,headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    all_link = soup.find('div', class_='nav-links').find_all('a')
    num = all_link[-2]['href'].split('/')[-2]
    return int(num)


# 获取开始页面每页中所有的图片的详细连接
def get_meizi_link_in_start_page(page_num):
    page_link = 'http://www.mzitu.com/page/' + str(page_num)
    html=requests.get(page_link,headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    meizi_links = []
    for li in soup.find('ul', id='pins').find_all('li'):
        link = li.find('span').find('a')
        tmp = Meizi(change_coding(link.get_text()), link['href'])
        meizi_links.append(tmp)
    return meizi_links


# 主程序
def start_mzitu():
    print('\nStart')
    has_down_list = get_all_has_down()
    """
    # 使用主页下载图片
    max_page_num=get_max_page_num()
    max_page_num = 5
    for page_num in range(max_page_num):
        meizi_links = get_meizi_link_in_start_page(page_num + 1)
    """
    all_meizi = get_all_meizi()
    for meizi in all_meizi:
        if meizi.link not in has_down_list:
            printGreen('meizi_index_title :  ' + meizi.title + '\n')
            printGreen('meizi_index_link  :  ' + meizi.link + '\n')
            try:
                max_num, first_down_link, category, date = get_other_info(meizi.link)
                meizi.category = category
                meizi.date = date
                down_link_list = get_down_link_list_by_str(first_down_link, max_num)
                printGreen('image_start_link  :  ' + down_link_list[0] + '\n')
                printGreen('image_max_num     :  ' + str(max_num) + '\n')
                down_image_list(down_link_list, meizi.id)
                insert_to_has_down(meizi)
                time.sleep(5)
            except:
                insert_to_error_down(meizi)
            print()
    print('End')


if __name__ == '__main__':
    all_mz = get_all_meizi()
    for mz in all_mz:
        print(mz.id,end='   ')
        print(mz.title)
        insert_to_has_down(mz)
