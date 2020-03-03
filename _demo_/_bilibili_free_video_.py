import requests

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

for page in range(1, 99):
    response = requests.get(url.format(page))
    response = response.json()
    data = response.get('data')
    if not data.get('has_next'):
        print(f'\n max page {page} \n')
        break
    for video in data.get('list'):
        badge = video.get('badge')
        if badge in ['限时免费']:
            print(f"{video['title']:<20} | {video['order']:<15} | {video['link']}")
