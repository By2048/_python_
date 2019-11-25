#!/root/.pyenv/versions/shell/bin/python

import os
import sys

if len(sys.argv) == 1:
    print('update|更新配置 / reset|还原配置')
    sys.exit()

arg = sys.argv[1]

if arg == 'update':
    command = 'cp /root/backup/oh-my-zsh/robbyrussell.zsh-theme ~/.oh-my-zsh/themes/robbyrussell.zsh-theme'
    os.system(command)

if arg == 'reset':
    command = 'cp /root/backup/oh-my-zsh/robbyrussell.zsh-theme.bk ~/.oh-my-zsh/themes/robbyrussell.zsh-theme'
    os.system(command)

print(123)

command = 'exec $SHELL'
os.system(command)
