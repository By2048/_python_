import os
import re

dytt_title = ".*\[(.*)\].*"
# # dytt_title = re.compile('\[.*\]')

name_0 = r"罗拉快跑BD国德双语中字[电影天堂www.dy2018.com].mkv"
name_1 = r"[电影天堂www.dy2018.com]罗拉快跑BD国德双语中字.mkv"
name_ = [name_0, name_1]

for name in name_:
    print(re.findall(dytt_title, name))

string = "xxxxxxxxxxxxxxxxxxxxxxxx entry '某某内容' for aaaaaaaaaaaaaaaaaa"

result = re.findall(".*entry(.*)for.*", string)
for x in result:
    print(x)


print('-'*88)


video_get=r"T:\ffmpeg.exe -f concat -i G:\_Test\Download\17693302\1\video_list.txt -c copy G:\_Test\Video\Python3爬虫实战 课时.flv"