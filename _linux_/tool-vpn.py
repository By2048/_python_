#!/root/.pyenv/versions/shell/bin/python

import os
import sys

arg = sys.argv[1] if len(sys.argv) >= 2 else None


def _help_():
    print("show|显示当前端口 \ change {port}|修改端口 \ restart \ stop \ start")


def _show_():
    command = 'docker ps --format "{{.Ports}}" --filter name=vpn'
    response = os.popen(command).read()
    response = response.lstrip('0.0.0.0:').split('->')[0]
    print(response)


def _run_():
    os.system(f'docker {arg} vpn')


def _change_():
    arg_2 = sys.argv[2] if len(sys.argv) >= 3 else None
    if not arg_2:
        return

    command = 'docker stop vpn && docker rm vpn'
    os.popen(command).read()

    command = f"docker run -d --name vpn --restart=always -p {arg_2}:2048 " \
              f"oddrationale/docker-shadowsocks " \
              f"-s 0.0.0.0 -p 2048 -k SSDK65gh55fj10VV -m aes-256-cfb"
    os.popen(command).read()

    command = 'docker ps -a | grep vpn'
    os.system(command)


data = {
    None: _help_,
    'help': _help_,
    'show': _show_,
    'restart': _run_,
    'stop': _run_,
    'start': _run_,
    'change': _change_
}
data.get(arg)()
