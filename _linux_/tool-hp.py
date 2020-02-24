#!/root/.pyenv/versions/shell/bin/python

import os
import sys

arg = sys.argv[1] if len(sys.argv) >= 2 else None


def _help_():
    print("update|更新脚本")


def _update_():
    os.system('curl https://cht.sh/:cht.sh > /root/bin/hp')
    os.system('chmod +x /root/bin/hp')


data = {
    None: _help_,
    'help': _help_,
    'update': _update_
}
data.get(arg)()
