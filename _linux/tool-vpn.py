#!/root/.pyenv/versions/shell/bin/python

import os
import sys

if len(sys.argv) == 1:
    print("show|显示当前端口 \ {port}|修改端口 \ restart \ stop \ start")
    sys.exit()

arg = sys.argv[1]

if arg == 'show':
    command = 'docker ps --format "{{.Ports}}" --filter name=vpn'
    response = os.popen(command).read()
    response = response.lstrip('0.0.0.0:').split('->')[0]
    print(response)

if arg in ['restart', 'stop', 'start']:
    os.system(f'docker {arg} vpn')

if arg.isdigit():
    command = 'docker stop vpn && docker rm vpn'
    os.popen(command).read()

    command = f"docker run -d --name vpn --restart=always -p {arg}:2048 " \
              f"oddrationale/docker-shadowsocks " \
              f"-s 0.0.0.0 -p 2048 -k SSDK65gh55fj10VV -m aes-256-cfb"
    os.popen(command).read()

    command = 'docker ps -a | grep vpn'
    os.system(command)
