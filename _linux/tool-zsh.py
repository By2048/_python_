#!/root/.pyenv/versions/shell/bin/python

import os
import shutil
import sys

arg = sys.argv[1] if len(sys.argv) >= 2 else None

backup = r'/root/backup/oh-my-zsh'

files = [
    {
        'path': f"/root/.oh-my-zsh/themes/robbyrussell.zsh-theme",
        'replace': ('%c', '$PWD')
    }
]

if not os.path.exists(backup):
    os.makedirs(backup)


def _help_():
    print('update|更新配置 / reset|还原配置')


def _update_():
    for file in files:
        print(f"{file['path']}    {file['replace'][0]} -> {file['replace'][1]}")
        origin_file = file['path']
        backup_file = f"{backup}/{os.path.basename(origin_file)}"

        if not os.path.isfile(backup_file):
            shutil.copy(origin_file, backup_file)

        with open(backup_file, 'r', encoding='utf-8') as backup_data:
            _0, _1 = file['replace'][0], file['replace'][1]
            backup_data = backup_data.read().replace(_0, _1)

        with open(origin_file, 'w+', encoding='utf-8') as origin_data:
            for item in backup_data:
                origin_data.write(item)

    os.system('exec $SHELL')


def _reset_():
    for item in os.listdir(backup):
        backup_path = os.path.join(backup, item)
        for file in files:
            if os.path.basename(file['path']) == item:
                print(f"{backup_path} -> {file['path']}")
                shutil.move(backup_path, file['path'])
                break
    os.system('exec $SHELL')


data = {
    None: _help_,
    'help': _help_,
    'update': _update_,
    'reset': _reset_,
}
data.get(arg)()
