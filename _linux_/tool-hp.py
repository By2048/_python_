#!/root/.pyenv/versions/_python_/bin/python

import os

import fire


def help():
    print("update|更新脚本")


def update():
    os.system('curl https://cht.sh/:cht.sh > /root/bin/hp')
    os.system('chmod +x /root/bin/hp')


if __name__ == '__main__':
    fire.Fire()
