import os
import json
import shutil


start_path = 'F:\\bilibili'

end_path='F:\\Video\\BillBill'

# 将后缀名 .blv 替换成 .flv
def replace_blv_to_flv():
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith(('.blv')):
                old_name=os.path.join(root, file)
                new_name=old_name.replace('.blv','.flv')
                print(old_name+'\n'+new_name+'\n')
                os.rename(old_name, new_name)

def get_all_video_path():
    all_video_path = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.endswith(('.flv', '.mp4')):
                all_video_path.append(os.path.join(root, file))
    return all_video_path


def get_video_json_path(video_path):
    path_list = video_path.split('\\')[:-2]
    json_path = video_join(path_list) + 'entry.json'
    return json_path


def get_folder_num(folder_path):
    folder_num = 0
    folders = os.listdir(folder_path)
    for folder in folders:
        if os.path.isdir(os.path.join(folder_path, folder)) == True:
            folder_num += 1
    return folder_num


def get_video_num(video_path):
    video_num = 0
    for file in os.listdir(video_path):
        if file.endswith(('.mp4', '.flv')):
            video_num += 1
    return video_num


def video_join(paths):
    out_path = ''
    for path in paths:
        if path != '':
            out_path = out_path + path + '\\'
    return out_path


def get_video_name(original_name, json_path):
    video_name = ''
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            date = json.load(file)
            video_page = date['page_data']['page']
            video_name += date['title']
            video_name = video_name.replace('/', ' ').replace('\\', ' ')
            if video_page != 1:
                video_name += str(video_page - 1)
            # print(video_name +" -> + str(date['avid']))
            video_name += ' ' + original_name
            video_name = change_name(video_name)
    except:
        pass
    return video_name


def change_name(old_name):
    new_name = old_name\
        .replace('?', '')\
        .replace('？', '')\
        .replace('【', '[')\
        .replace('】', ']')\
        .replace('| ','')\
        .replace('*','')
    return new_name


def move_video():
    all_video_path = get_all_video_path()

    for path in all_video_path:
        file_name=os.path.basename(path)

        new_path=end_path+'\\'+file_name
        print(path+'\n'+new_path+'\n')
        shutil.move(path,new_path)


def hava_next_file(curr_path):
    folder_path,base_name= os.path.split(curr_path)
    next_name=''
    if base_name.endswith('.mp4'):
        next_name=base_name.replace('0.mp4','1.mp4')
    elif base_name.endswith('.flv'):
        next_name=base_name.replace('0.flv','1.flv')
    next_path=folder_path+'\\'+next_name

    return os.path.isfile(next_path)


def replace_0():
    for root, dirs, files in os.walk(end_path):
        for file in files:
            old_name = os.path.join(root, file)
            if file.endswith(' 0.flv') and hava_next_file(old_name)==False:
                new_name=old_name.replace(' 0.flv','.flv')
                print(old_name+'\n'+new_name+'\n')
                os.rename(old_name,new_name)

            if file.endswith(' 0.mp4') and hava_next_file(old_name)==False:
                new_name=old_name.replace(' 0.mp4','.mp4')
                print(old_name+'\n'+new_name+'\n')
                os.rename(old_name,new_name)



if __name__ == '__main__':
    replace_blv_to_flv()
    all_video_path = get_all_video_path()

    for video_path in all_video_path:
        json_path = get_video_json_path(video_path)
        video_name = get_video_name(os.path.basename(video_path), json_path)
        video_new_path = os.path.dirname(video_path) + '\\' + video_name
        os.rename(video_path, video_new_path)

    move_video()
    replace_0()
