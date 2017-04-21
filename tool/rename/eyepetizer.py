import os

video_path=r'F:\\Video\\Eyepetizer\\'

for name in os.listdir(video_path):
    print('->'+name)


for name in os.listdir(video_path):
    old_name=video_path+name
    new_name=video_path+name+'.mp4'
    print(old_name+"   "+new_name)
    os.rename(old_name,new_name)

for name in os.listdir(video_path):
    old_name=video_path+name
    new_name=(video_path+name)[:-4]
    print(old_name+"   "+new_name)
    # os.rename(old_name,new_name)