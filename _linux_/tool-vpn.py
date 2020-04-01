#!/root/.pyenv/versions/_python_/bin/python

import os
import sys

import fire


def help():
    print("                show | 显示当前端口")
    print("change --port={port} | 修改端口")


def show():
    command = 'docker ps --format "{{.Ports}}" --filter name=vpn'
    response = os.popen(command).read()
    response = response.lstrip('0.0.0.0:').split('->')[0]
    print(response)


def change(port):
    command = 'docker stop vpn && docker rm vpn'
    os.popen(command).read()

    os.system('docker pull oddrationale/docker-shadowsocks')

    command = f"docker run -d --name vpn --restart=always -p {port}:2048 " \
              f"oddrationale/docker-shadowsocks " \
              f"-s 0.0.0.0 -p 2048 -k SSDK65gh55fj10VV -m aes-256-cfb"
    os.popen(command).read()

    command = 'docker ps -a | grep vpn'
    os.system(command)


if __name__ == '__main__':
    fire.Fire()
