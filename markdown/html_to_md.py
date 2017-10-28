from bs4 import *
import functools
import sys


def get_lines_num():
    num = len(soup.find('tr').find_all('th'))
    if num == 0:
        num = len(soup.find('tr').find_all('td'))
    return num


def create_md_title(num):
    line = '|'
    for th in soup.find('tr').find_all('th'):
        if len(soup.find('tr').find_all('th')) != 0:
            line += ' ' + th.get_text() + ' |'
    if line != '|':
        line_1 = line.replace('\n', '')
        lines.append(line_1)
    else:
        line_1 = ('     ').join('|' * (num + 1))
        lines.append(line_1)

    line_2 = (' --- ').join('|' * (num + 1))

    lines.append(line_2)


def get_main_body():
    for tr in soup.find_all('tr'):
        line = '|'
        for td in tr.find_all('td'):
            if len(tr.find_all('td')) != 0:
                if td.find('ul') != None:
                    ul_str = ''
                    for li in td.find('ul').find_all('li'):
                        ul_str += ' ' + li.get_text()
                    line += ' ' + ul_str + ' |'
                else:
                    line += ' ' + td.get_text() + ' |'
        if line != '|':
            line = line.replace('\n', '')
            line = line.replace('<', '\<')
            lines.append(line)

if __name__ == '__main__':

    print('\n输入以 ==== 结束\n')

    html_str = ''
    str_in = []
    lines = []

    sentinel = '===='  # 遇到这个就结束
    for line in iter(input, sentinel):
        str_in.append(line)
    for item in str_in:
        html_str += item

    soup = BeautifulSoup(html_str, "lxml")

    num = get_lines_num()
    create_md_title(num)
    get_main_body()

    for line in lines:
        print(line)
