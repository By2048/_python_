from io import BytesIO

import requests
from PIL import Image

url = 'http://i0.hdslb.com/bfs/bangumi/image/aad797f1f0212aba5578a1ed1c992ef1b9ff7c4b.jpg'


def test_1():
    img = Image.open(requests.get(url, stream=True).raw)
    img.show()


def test_2():
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


def test():
    pass


if __name__ == '__main__':
    test()
