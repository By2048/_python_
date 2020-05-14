import functools
from collections import namedtuple

from bs4 import BeautifulSoup

path = './___/bilibili.html'

Video = namedtuple('video', ['index', 'title'])


def compare(v1, v2):
    """ 13 > 13.5 """

    if '.' not in v1.index and '.' not in v2.index:
        return float(v1.index) - float(v2.index)

    if '.' in v1.index or '.' in v2.index:
        if int(float(v1.index)) == int(float(v2.index)):
            return len(v2.index) - len(v1.index)

    return 0


def info(videos):
    print()
    for item in videos:
        print(f"{item.index} {item.title}")


def main():
    with open(path, 'r', encoding='utf-8') as file:
        data = ''.join(file.readlines())
        data = BeautifulSoup(data, 'lxml')

    result = []
    for item in data.find_all('li'):
        index = item.find('div', class_='misl-ep-index').get_text()
        title = item.find('div', class_='misl-ep-title').get_text()
        index = '0' + index if len(index) == 1 else index
        video = Video(index, title)
        result.append(video)

    result = sorted(result, key=functools.cmp_to_key(compare))

    info(result)


def test():
    pass


if __name__ == '__main__':
    main()
