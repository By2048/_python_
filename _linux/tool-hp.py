#!/root/.pyenv/versions/shell/bin/python

import os
import sys

if len(sys.argv) == 1:
    print("update|更新脚本")
    sys.exit()

arg = sys.argv[1]

if arg == 'update':
    os.system('curl https://cht.sh/:cht.sh > /root/bin/hp')
    os.system('chmod +x /root/bin/hp')
