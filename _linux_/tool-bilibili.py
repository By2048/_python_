#!/root/.pyenv/versions/_python_/bin/python

import json
import os
import sys

import requests
from veryprettytable import VeryPrettyTable
import fire

bilibili_old = {}  # 上一次获取的数据
bilibili_new = {}  # 本次获取的数据

path = '/tmp/bilibili.json'
if sys.platform == 'win32':
    path = 't:\\bilibili.json'


def free():
    url = 'https://api.bilibili.com/pgc/season/index/result' \
          '?season_version=-1' \
          '&area=-1' \
          '&is_finish=-1' \
          '&copyright=-1' \
          '&season_status=-1' \
          '&season_month=-1' \
          '&year=-1' \
          '&style_id=-1' \
          '&order=1' \
          '&st=1' \
          '&sort=0' \
          '&page={}' \
          '&season_type=1' \
          '&pagesize=50' \
          '&type=1'

    # order
    # 0 更新时间
    # 1 无
    # 2 播放数量
    # 3 追番人数
    # 4 最高评分
    # 5 开播时间

    global bilibili_old
    global bilibili_new

    page = 1
    table = VeryPrettyTable(["Name", "Url"])
    table.header = False
    table.align["Name"] = "r"
    table.align["Url"] = "l"
    print()
    while True:
        print(f"\r Page... {page}", end="")
        response = requests.get(url.format(page))
        response = response.json()
        data = response.get('data')
        for video in data.get('list'):
            badge = video.get('badge')
            if badge in ['限时免费']:
                table.add_row([video['title'], video['link']])
                bilibili_new[video['media_id']] = {
                    'title': video['title'], 'link': video['link']}
        page += 1
        if not data.get('has_next') or page > 99:
            break

    print()
    print(table)

    # 与上一次获取的数据进行比较，输出有差异的数据
    if os.path.exists(path):
        with open(path, encoding='utf-8') as file:
            bilibili_old = json.load(file)

    table.clear_rows()

    check = False
    for new_id in bilibili_new:
        if str(new_id) not in bilibili_old:
            check = True
            table.add_row([
                bilibili_new[new_id]['title'],
                bilibili_new[new_id]['link']
            ])
    if check:
        print()
        print(table)

    # 存储本次获取的数据
    with open(path, 'w+', encoding='utf-8') as file:
        json.dump(bilibili_new, file)


def help():
    print('help | 命令帮助')
    print('free | 获取限时免费列表')


if __name__ == '__main__':
    fire.Fire()
