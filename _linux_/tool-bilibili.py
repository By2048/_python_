#!/root/.pyenv/versions/_python_/bin/python


import requests
import fire
from veryprettytable import VeryPrettyTable


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

    page = 1
    table = VeryPrettyTable(["Name", "Url"])
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
        page += 1
        if not data.get('has_next') or page > 99:
            break
    table.header = False
    print()
    print(table)


def help():
    print('help | 命令帮助')
    print('free | 获取限时免费列表')


if __name__ == '__main__':
    fire.Fire()
