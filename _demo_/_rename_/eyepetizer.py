import os
import sys
import sqlite3
import urllib
from urllib import request
import json


video_path='F:\\eyepetizer\\download\\video\\'
db_path='F:\\eyepetizer\\download\\download_manager.db'

json_link='http://baobab.kaiyanapp.com/api/v1/video/'

class Video:
    Id=''
    OldName=''
    NewName=''
    def __init__(self,id,oldName,newName):
        self.Id=id
        self.OldName=oldName
        self.NewName=newName


all_video=[]

cx = sqlite3.connect(db_path)
cu=cx.cursor()
cu.execute("select content_id,filepath from tasks")
all_data=cu.fetchall()

for data in all_data:
    all_video.append(Video(data[0],data[1].split('/')[-1],''))


for video in all_video:
    link=json_link+str(video.Id)

    response = request.urlopen(link)
    page = response.read()
    page = page.decode('utf-8')

    json_data = json.loads(page)
    video.NewName=json_data['title']


for video in all_video:
    old_path=video_path+video.OldName
    new_path=video_path+video.NewName+'.mp4'
    os.rename(old_path, new_path)
    print(old_path+'  '+new_path)
