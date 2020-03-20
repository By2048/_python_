import requests
from bs4 import BeautifulSoup


def test_1():
    url = r'https://help.aliyun.com/noticelist/9213612.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    result = []
    for item in soup.find_all('li', class_='y-clear'):
        print(item.find('a')['href'], item.find('a').get_text())
        result.append(item.find('a')['href'])
    return result


if __name__ == '__main__':
    test_1()
