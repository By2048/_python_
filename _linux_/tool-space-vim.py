#!/root/.pyenv/versions/_python_/bin/python

import os
import shutil

import fire

install = r'/root/.SpaceVim'
backup = r'/root/backup/SpaceVim'

files = [
    {'path': f"{install}/autoload/SpaceVim/layers/ui.vim", 'replace': ('<F2>', '<F3>')},
    {'path': f"{install}/config/plugins/vim-startify.vim", 'replace': ('<F2>', '<F3>')},

    {'path': f"{install}/autoload/SpaceVim/layers/core.vim", 'replace': ('<F3>', '<F2>')},
    {'path': f"{install}/config/plugins_before/defx.vim", 'replace': ('<F3>', '<F2>')},
    {'path': f"{install}/config/plugins_before/vimfiler.vim", 'replace': ('<F3>', '<F2>')}
]

if not os.path.exists(backup):
    os.makedirs(backup)


def help():
    print("replace | 快捷键替换")
    print("  reset | 快捷键还原")


def replace():
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


def reset():
    for item in os.listdir(backup):
        backup_path = os.path.join(backup, item)
        for file in files:
            if os.path.basename(file['path']) == item:
                print(f"{backup_path} -> {file['path']}")
                shutil.move(backup_path, file['path'])
                break


if __name__ == '__main__':
    fire.Fire()
