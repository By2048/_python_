#!/root/.pyenv/versions/shell/bin/python

import os
import sys

arg = sys.argv[1] if len(sys.argv) >= 2 else None


def _help_():
    print('update|更新配置 / reset|还原配置')


def _update_():
    command = 'cp /root/backup/oh-my-zsh/robbyrussell.zsh-theme /root/.oh-my-zsh/themes/robbyrussell.zsh-theme'
    os.system(command)
    os.system('exec $SHELL')


def _reset_():
    command = 'cp /root/backup/oh-my-zsh/robbyrussell.zsh-theme.bk /root/.oh-my-zsh/themes/robbyrussell.zsh-theme'
    os.system(command)
    os.system('exec $SHELL')


data = {
    None: _help_,
    'help': _help_,
    'update': _update_,
    'reset': _reset_,
}
data.get(arg)()
