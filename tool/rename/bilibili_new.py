import os
import json
import shutil


# 根据文件夹中的 entry.json 获取视频的名字
def get_name_by_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        _title = json_data['title']
        try:
            _name = json_data['page_data']['part']
        except:
            _name = ''
        video_name = _title + '_' + _name
    return video_name


# 使用 ffmpeg 拼接视频
def get_sum_video(ffmpeg_path, video_list_path, new_video_path):
    join_video = "{0} -f concat -safe 0 -i {1} -c copy {2}".format(ffmpeg_path, video_list_path, new_video_path)
    print(join_video + '\n')
    os.system(join_video)


# 在每个视频文件夹路径下获取 video_list.txt
def get_video_list(folder_path):
    file_line = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.blv')):
                shutil.move(os.path.join(root, file), folder_path)
    for file in os.listdir(folder_path):
        if file.endswith(('.blv')):
            old_name = os.path.join(folder_path, file)
            new_name = old_name.replace('.blv', '.flv')
            os.rename(old_name, new_name)

    for file in os.listdir(folder_path):
        if file.endswith(('.flv')):
            file_line.append(os.path.join(folder_path, file))
    file_line.sort(key=lambda x: int(os.path.basename(x).split('.')[0]),reverse=False)

    video_list_path = os.path.join(folder_path, 'video_list.txt')
    with open(video_list_path, 'w+', encoding='utf-8') as file:
        for line in file_line:
            file.write('file' + ' ' + '\'' + line + '\'')
            file.write('\n')

    return video_list_path


if __name__ == '__main__':
    # start_path = r'G:\_Test\Download\17693302'
    # end_path = r'G:\_Test\Video'
    # ffmpeg_path = r'T:\ffmpeg.exe'

    start_path = 'T:\\4736'
    end_path = 'T:\\'
    ffmpeg_path = 'T:\\ffmpeg.exe'

    # 处理文件
    for file in os.listdir(start_path):
        folder_path = os.path.join(start_path, file)
        video_list_path = get_video_list(folder_path)

        json_path = os.path.join(folder_path, 'entry.json')
        video_name = get_name_by_json(json_path)
        new_video_path = os.path.join(end_path, video_name) + '.flv'
        get_sum_video(ffmpeg_path, video_list_path, new_video_path)
