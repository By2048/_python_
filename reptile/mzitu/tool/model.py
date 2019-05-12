import logging
from datetime import datetime

try:
    from mzitu.tool.format import get_zh_num
except ImportError:
    from tool.format import get_zh_num


class Meizi:
    def __init__(self, id: int, title: str, link: str, category=[], date='', downloads=[]):
        self.id = id
        self.title = title
        self.link = link
        self.category = category
        self.date = date
        self.downloads = downloads

    def __repr__(self):
        zh_num = 60 - get_zh_num(self.title)
        return '{0:<{1}} {2:<50}'.format(self.title, zh_num, self.link)

    def serialization(self):
        data = {
            'id': self.id,
            'name': self.title,
            'link': self.link,
            'category': self.category,
            'date': self.date,
            'downloads': self.downloads
        }
        return data

    def deserialization(self, data):
        id = data.get('id')
        name = data.get('name')
        link = data.get('link')
        category = data.get('category')
        date = data.get('date')
        downloads = data.get('downloads')

        return Meizi(id, name, link, category, date, downloads)


def __getitem__(self, item):
    return self.downloads[item]


class MImage:
    def __init__(self, name: str, path: str, type: str, size: float, width: int, heigth: int,
                 visit_date: datetime, create_date: datetime, change_date: datetime):
        self.name = name
        self.path = path
        self.type = type
        self.size = size
        self.width = width
        self.height = heigth
        self.visit_date = visit_date
        self.create_date = create_date
        self.change_date = change_date

    def __str__(self):
        logging.info('{0:<15}{1}'.format('name', self.name))
        logging.info('{0:<15}{1}'.format('path', self.path))
        logging.info('{0:<15}{1}'.format('type', self.type))
        logging.info('{0:<15}{1}'.format('size', self.size))
        logging.info('{0:<15}{1}'.format('width', self.width))
        logging.info('{0:<15}{1}'.format('height', self.height))
        logging.info('{0:<15}{1}'.format('visit_date', self.visit_date))
        logging.info('{0:<15}{1}'.format('create_date', self.create_date))
        logging.info('{0:<15}{1}'.format('change_date', self.change_date))


class MFolder:
    def __init__(self, folder_name: str, folder_path: str, create_date: datetime, image_num: int, total_size: float):
        self.name = folder_name
        self.path = folder_path
        self.date = create_date
        self.num = image_num
        self.size = total_size

    def __str__(self):
        logging.info('{0:<10}{1}'.format('name', self.name))
        logging.info('{0:<10}{1}'.format('path', self.path))
        logging.info('{0:<10}{1}'.format('date', self.date))
        logging.info('{0:<10}{1}'.format('num', self.num))
        logging.info('{0:<10}{1}'.format('size', self.size))


def test():
    pass


if __name__ == '__main__':
    test()
