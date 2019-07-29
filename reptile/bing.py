import sys
import os
import logging

import requests

try:
    import _conf
except ImportError as e:
    pass

if sys.platform == "linux":
    keep_path = "/root/ftp/bing"
elif sys.platform == "win32":
    keep_path = "E:\\Image\\Bing"
else:
    raise Exception(f"设置 keep_path 失败 sys.platform:{sys.platform}")

"""
http://stackoverflow.com/questions/10639914/is-there-a-way-to-get-bings-photo-of-the-day
http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US
"""


class Image:
    def __init__(self, date, link, title):
        self.date = date
        self.link = link
        self.title = title

    def __str__(self):
        return f'{self.title}    {self.link}    {self.date}'

    def __repr__(self):
        return f'{self.title}'

    @property
    def name(self):
        _date = self.date
        _title = self.title
        _type = self.link.split('.')[-1].replace('&pid=hp', '')
        name = f'{_date[0:4]}-{_date[4:6]}-{_date[6:8]} {_title}.{_type}'
        return name

    @property
    def path(self):
        return os.path.join(keep_path, self.name)


def get_image(idx=0, n=1):
    data = requests.get(f'http://www.bing.com/HPImageArchive.aspx?format=js&idx={idx}&n={n}&mkt=en-US').json()
    result = []
    for i in range(n):
        try:
            _date = data['images'][i]['enddate']
            _title = data['images'][i]['copyright'].replace('/', ' ')
            _link = f'http://www.bing.com' + data['images'][i]['url']
            result.append(Image(_date, _link, _title))
        except KeyError as e:
            logging.exception(e)
    return result


def download_image(image: Image):
    response = requests.get(image.link)
    with open(image.path, "wb") as file:
        file.write(response.content)


if __name__ == '__main__':
    logging.info('Start')

    images = get_image(idx=0, n=7)
    for image in images:
        if os.path.isfile(image.path):
            continue
        logging.info(image)
        download_image(image)

    logging.info('End')
