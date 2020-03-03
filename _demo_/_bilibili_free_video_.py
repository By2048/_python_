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
      '&order=2' \
      '&st=1' \
      '&sort=0' \
      '&page={}' \
      '&season_type=1' \
      '&pagesize=50' \
      '&type=1'

for page in range(1, 999):
    response = requests.get(url.format(page))
    response = response.json()
    data = response.get('data')
    if not data.get('has_next'):
        break
    for video in data.get('list'):
        badge = video.get('badge')
        if badge in ['限时免费']:
            print(f"{video['title']:<20} | {video['order']:<15} | {video['link']}")
