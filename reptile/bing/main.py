import sys
import os
import logging

import requests

if sys.platform == "linux":
    keep_path = "/root/share/bing"
elif sys.platform == "win32":
    keep_path = "R:\\Image\\bing"
else:
    keep_path = ''
    raise Exception(f"获取 keep_path 失败 sys.platform = {sys.platform}")


class BImage:
    def __init__(self, date, link, title):
        self.date = date
        self.link = link
        self.title = title

    def __repr__(self):
        return f'{self.title}    {self.link}    {self.date}'


def get_image(idx=0, n=1):
    api_url = f'http://www.bing.com/HPImageArchive.aspx?format=js&idx={idx}&n={n}&mkt=en-US'
    data = requests.get(api_url).json()
    # data = urllib.request.urlopen(api_url).read().decode('utf-8')
    # data = json.loads(data)
    images = []
    for i in range(n):
        try:
            _date = data['images'][i]['enddate']
            _title = data['images'][i]['copyright'].replace('/', ' ')
            _link = f'http://www.bing.com' + data['images'][i]['url']
            images.append(BImage(_date, _link, _title))
        except KeyError:
            pass
    return images


def get_image_name(image: BImage):
    _date = image.date
    _title = image.title
    _type = image.link.split('.')[-1]
    name = f'{_date[0:4]}-{_date[4:6]}-{_date[6:8]} {_title}.{_type}'
    return name


def test():
    # api detail link = http://stackoverflow.com/questions/10639914/is-there-a-way-to-get-bings-photo-of-the-day
    # api = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US'
    pass


if __name__ == '__main__':
    logging.info('Start')

    images = get_image(idx=0, n=7)

    for image in images:
        image_path = os.path.join(keep_path, get_image_name(image))
        if os.path.isfile(image_path):
            continue
        logging.info(f'{image.date} {image.title}')
        response = requests.get(image.link)
        with open(image_path, "wb") as file:
            file.write(response.content)

    logging.info('End')
