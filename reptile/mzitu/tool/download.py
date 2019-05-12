import os
import sys
import urllib
import logging
import shutil
import urllib.request
import multiprocessing

import requests

try:
    from mzitu.conf.base import download_path
    from mzitu.tool.model import Meizi
except ImportError:
    from conf.base import download_path
    from tool.model import Meizi

pool_num = 4


def _download_image(link: str, path: str):
    """ 下载图片

    :param link: 图片的下载链接
    :param path: 图片的保存路径
    :return:
    """

    def call_back(blocknum, blocksize, totalsize):
        """ 下载回显

        :param blocknum: 已经下载的数据块
        :param blocksize: 数据块的大小
        :param totalsize: 远程文件的大小
        :return:
        """
        percent = 100.0 * blocknum * blocksize / totalsize
        sys.stdout.write("\rDownloading : %.2f%%\r" % percent)
        sys.stdout.flush()
        if percent >= 100:
            sys.stdout.write("\rDownloading : %.2f%% -> " % 100)
            print('Download_Success ')

    try:
        urllib.request.urlretrieve(link, path, call_back)
    except Exception as e:
        logging.error("下载失败,下载链接 {0} ".format(link))


def _download_images(links: list, path: str):
    """ 下载一组图片 一个连接下所有图片

    :param links:
    :param path:
    :return:
    """
    pool = multiprocessing.Pool(processes=pool_num)
    for link in links:
        pool.apply_async(_download_image, (link, path))
    pool.close()
    pool.join()


# 使用reqursts下载图片
def download_meizi(meizi: Meizi):
    def create_download_path(id: int) -> str:
        path = os.path.join(download_path, str(id))
        if not os.path.exists(path):
            os.makedirs(path)
            return path
        else:
            logging.info('下载路径 {0} 已经存在'.format(path))

    def delete_download_path(id: int):
        path = os.path.join(download_path, str(id))
        try:
            shutil.rmtree(path)
        except Exception as e:
            logging.exception(e)

    def rename_download_path(id: int, title: str):
        """ 下载完成后将ID名下载路径转换为文件名

        :param id: 图片组的ID
        :param title: 图片组的文件名
        """

        try:
            _old = os.path.join(download_path, str(id))
            _new = os.path.join(download_path, title)
            os.rename(_old, _new)
        except Exception as e:
            logging.info('重命名错误')
            logging.exception(e)

    def get_header(download_link: str):
        header = {
            'Host': 'i.meizitu.net',
            'Pragma': 'no-cache',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5)'
                           'AppleWebKit/537.36 (KHTML, like Gecko)'
                           'Chrome/59.0.3071.115 Safari/537.36'),
            'Accept': 'image-test/webp,image-test/apng,image-test/*,*/*;q=0.8',
            'Referer': '{0}'.format(download_link),
        }
        return header

    images_path = create_download_path(meizi.id)
    for download in meizi.downloads:
        image_keep_path = os.path.join(images_path, os.path.basename(download))
        try:
            with open(image_keep_path, "wb+") as file:
                response = requests.get(download, headers=get_header(download))
                file.write(response.content)
        except Exception as e:
            logging.error(f'下载图片出错，图片下载位置 {images_path}')
            logging.exception(e)

    rename_download_path(meizi.id, meizi.title)


if __name__ == '__main__':
    pass
