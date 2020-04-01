#!/root/.pyenv/versions/_python_/bin/python

import os
import shutil

path_src = '/root/deployment/_python_/_linux_'
path_dsc = '/root/bin'

for item in os.listdir(path_dsc):
    file_dst = os.path.join(path_dsc, item)
    if not os.path.exists(file_dst):
        continue
    os.remove(file_dst)

for item in os.listdir(path_src):
    file_src = os.path.join(path_src, item)
    file_dst = os.path.join(path_dsc, item).rstrip('.py')

    if os.path.exists(file_dst):
        os.remove(file_dst)

    if item in ['__init__.py']:
        continue

    shutil.copy(file_src, file_dst)

    os.system(f"chmod +x {file_dst}")
    os.system(f"dos2unix {file_dst}")  # fix python ^M error
