import requests
import json


api_code='cbf61fb8197d5fdc054041c1bd2945e9'
link='https://wall.alphacoders.com/api2.0/get.php?auth=cbf61fb8197d5fdc054041c1bd2945e9&method=tag&id=218&page=10&info_level=2'


html_data=(requests.get(link).text)


json_data=json.loads(html_data)
print(json_data)
#
# # print['url_image'])
#
for item in json_data['wallpapers']:
    print(item)


