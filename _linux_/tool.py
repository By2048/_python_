#!/root/.pyenv/versions/shell/bin/python

import os
import shutil

# 直接进行脚本复制
path_tool = '/root/deployment/_python/_linux'
path_bin = '/root/bin'
if os.path.exists(path_tool) and os.path.exists(path_bin):
    shutil.rmtree(path_bin)
    shutil.copytree(path_tool, path_bin)

os.remove(os.path.join(path_bin, '__init__.py'))

# 脚本文件上传后内容修改
for item in os.listdir(path_bin):
    if item.endswith('.py'):
        _origin = os.path.join(path_bin, item)
        _change = _origin.replace('.py', '')
        os.rename(_origin, _change)
        os.system(f"chmod +x {_change}")
        os.system(f"dos2unix {_change}")  # fix python ^M error
