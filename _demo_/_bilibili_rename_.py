import re
import os

path = r"T:\理科生坠入情网，故尝试证明。"

videos = []


def main():
    for item in os.listdir(path):
        old = item
        item = item.split('.')
        index, name, file_type = item[0].zfill(2), item[1], item[2]
        name = ''.join(re.split(r'\([avAVpP,\d]+\)', name))  # 去除(Avxxxxxx,Pxxxxx)
        new = f"{index} {name}.{file_type}"
        print(old, '---', new)
        old = os.path.join(path, old)
        new = os.path.join(path, new)
        os.rename(old, new)


def test():
    print(re.split(r'\([avAVpP,\d]+\)', '1.使徒、袭来(Av14925009,P1).mp4'))
    videos = sorted(videos, key=lambda x: int(x[0:2]))

    # data = re.match(r'([\d]+)(\.)([\s\S]+)(^\(.*\)$)', name)
    # data = re.match(r'([\d]+)(\.)([\s\S]+)', name)
    # if data:
    #     print(data.groups())
    #
    # print(data)


if __name__ == '__main__':
    main()
