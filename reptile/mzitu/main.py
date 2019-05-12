import os
import time
import logging
from datetime import datetime

import requests
from bs4 import BeautifulSoup

try:
    from mzitu.conf.base import images_link, images_link_old, headers
    from mzitu.tool.sql import insert_download, get_downloads
    from mzitu.tool.model import MImage, MFolder, Meizi
    from mzitu.tool.download import download_meizi
except ImportError:
    from conf.base import images_link, images_link_old, headers
    from tool.sql import insert_download, get_downloads
    from tool.model import MImage, MFolder, Meizi
    from tool.download import download_meizi

logging.basicConfig(level=logging.INFO)


def get_meizi_other_info(meizi):
    # 获取图片的其他信息
    def get_image_num(soup):
        """ 获取一个页面的最大图片数量 方便合成连接

        :param soup:
        :return:
        """
        max_num = 0
        try:
            for span in soup.find('div', class_='pagenavi').find_all('span'):
                if (span.get_text() == '下一页»'):
                    max_num = span.parent.previous_sibling.find('span').get_text()
                    break
        except Exception as e:
            logging.error(f'获取最大数量图片失败 {meizi}')
            logging.exception(e)

        return int(max_num)

    def get_first_img_down_link(soup):
        """ 获取第一张图片下载的连接 """
        link = ''
        try:
            link = soup.find('div', class_='main-image').find('img')['src']
        except Exception as e:
            logging.error(f'get img link fail {meizi}')
            logging.exception(e)
        return link

    def get_categroy_date(soup):
        """ 获取图片的 分类 日期 """
        category, date = [], None
        try:
            spans = soup.find('div', class_='main-meta').find_all('span')
            category = spans[0].find('a').get_text()
            date = spans[1].get_text().replace('发布于 ', '')
        except Exception as e:
            logging.error(f'获取图片的分类或日期失败 {meizi}')

        try:
            date = datetime.strptime(date, '%Y-%m-%d %H:%M')
        except Exception as e:
            logging.error(f'转换日期失败{date}')

        return category, date

    def get_download_links(first_download_link, max_num):
        """ 通过字符串合成的方式获取下载链接
        http://i.meizitu.net/2017/10/29c02.jpg
        start_link   http://i.meizitu.net/2017/10
        image_name   29c02.jpg
        _name        29c
        _num         02
        _type        jpg
        """
        start_link, image_name = os.path.split(first_download_link)

        _name = image_name.split('.')[0][:-2]
        _num = int(image_name.split('.')[0][-2:])
        _type = image_name.split('.')[1]

        downloads = []
        for num in range(_num, _num + max_num):
            downloads.append(f'{start_link}/{_name}{str(num).zfill(2)}.{_type}')
        logging.info(f'first_download_link  :  {first_download_link}')
        logging.info(f'image_max_num        :  {max_num}')

        return downloads

    try:
        html = requests.get(meizi.link, headers=headers)
        soup = BeautifulSoup(html.text, "html.parser")
        max_num = get_image_num(soup)
        first_down_link = get_first_img_down_link(soup)
        meizi.category, meizi.date = get_categroy_date(soup)
        meizi.downloads = get_download_links(first_down_link, max_num)
    except Exception as e:
        logging.info(f'获取图片其他信息失败{meizi}')
        logging.exception(e)

    return meizi


def get_all_meizi():
    """ 获取 http://www.mzitu.com/all/ 下数据 """

    meizis, soup = [], None

    try:
        # html = requests.get(images_link, headers=headers)
        html = requests.get(images_link_old, headers=headers)
        soup = BeautifulSoup(html.text, "html.parser")
    except Exception as e:
        logging.error(f'获取网页失败 {images_link}')
        logging.exception(e)

    for ul in soup.find_all('ul', class_='archives'):
        for link in ul.find_all('a'):
            try:
                _id = int(link['href'].split('/')[-1])
                _title = link.get_text()
                _link = link['href']
                meizis.append(Meizi(_id, _title, _link))
            except Exception as e:
                logging.error(f'解析失败 {link}')
                logging.exception(e)

    return meizis


# 主程序
def main():
    already_downloads = get_downloads()
    meizis = get_all_meizi()

    for meizi in meizis:
        if meizi.id in already_downloads:
            continue
        try:
            logging.info(f'title                :  {meizi.title}')
            meizi = get_meizi_other_info(meizi)
            download_meizi(meizi)
            insert_download(meizi)
            logging.info('')
        except Exception as e:
            logging.error(f'处理失败{meizi}')
            insert_download(meizi, status=False)
        finally:
            time.sleep(16)


def test():
    # meizis = get_all_meizi()
    # for meizi in meizis:
    #     print(meizi)
    meizi = Meizi(id=170206, title='丝足控福利 气质美女小热巴丝袜美腿喷血诱人', link='https://www.mzitu.com/170206')

    get_meizi_other_info(meizi)


if __name__ == '__main__':
    main()
