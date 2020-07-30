import re
import os

path = ''  # 文件夹路径
videos = []  # 视频文件名


def info():
    try:
        from veryprettytable import VeryPrettyTable
    except ImportError:
        for video in videos:
            print(video[0], video[1])
        return
    table = VeryPrettyTable(['old', 'new'])
    table.align['old'] = 'l'
    table.align['new'] = 'l'
    for video in videos:
        table.add_row(video)
    print(table)


def init():
    print("\n粘贴文件夹路径\n")
    global path
    path = input()
    path = path.strip('"')

    def get_name(old_name):
        item = old_name.split('.')
        try:
            index, name, file_type = item[0].zfill(2), item[1], item[2]
        except Exception as e:
            print(f'\n文件名解析错误 {old_name}\n')
            return False
        video_title = ''.join(re.split(r'\([avAVpP,\d]+\)', name))  # 去除(Avxxxxxx,Pxxxxx)
        new_name = f"{index} {video_title}.{file_type}"
        return new_name

    if os.path.isfile(path):
        old = os.path.basename(path)
        path = os.path.dirname(path)
        new = get_name(old)
        videos.append([old, new])
        return True

    for item in os.listdir(path):
        old = item
        new = get_name(old)
        videos.append([old, new])
    return True


def rename():
    print('\n确认重命名\n')
    check = input()

    if check not in ('1', 'true', 'y', True) or not check:
        return

    for video in videos:
        if not video[0] or not video[1]:
            print(f'获取文件名错误 {video}')
            return
        old = os.path.join(path, video[0])
        new = os.path.join(path, video[1])
        os.rename(old, new)


def test():
    pass
    # print(re.split(r'\([avAVpP,\d]+\)', '1.使徒、袭来(Av14925009,P1).mp4'))
    # videos = sorted(videos, key=lambda x: int(x[0:2]))
    # data = re.match(r'([\d]+)(\.)([\s\S]+)(^\(.*\)$)', name)
    # data = re.match(r'([\d]+)(\.)([\s\S]+)', name)
    # print(data,data.groups())


if __name__ == '__main__':
    if init():
        info()
        rename()
