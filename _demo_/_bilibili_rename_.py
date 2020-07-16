import re
import os

path = ''
videos = []


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


def main():
    print("\n粘贴文件夹路径\n")
    global path
    path = input()
    for item in os.listdir(path):
        old = item
        item = item.split('.')
        index, name, file_type = item[0].zfill(2), item[1], item[2]
        name = ''.join(re.split(r'\([avAVpP,\d]+\)', name))  # 去除(Avxxxxxx,Pxxxxx)
        new = f"{index} {name}.{file_type}"
        videos.append([old, new])


def rename():
    print('\n确认重命名\n')
    check = input()
    if check not in ('1', 'true', 'y', True):
        return
    for video in videos:
        old = os.path.join(path, video[0])
        new = os.path.join(path, video[1])
        os.rename(old, new)
        print(old, new)


def test():
    pass
    # print(re.split(r'\([avAVpP,\d]+\)', '1.使徒、袭来(Av14925009,P1).mp4'))
    # videos = sorted(videos, key=lambda x: int(x[0:2]))
    # data = re.match(r'([\d]+)(\.)([\s\S]+)(^\(.*\)$)', name)
    # data = re.match(r'([\d]+)(\.)([\s\S]+)', name)
    # print(data,data.groups())


if __name__ == '__main__':
    main()
    info()
    rename()
