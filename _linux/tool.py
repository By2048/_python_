#!/root/.pyenv/versions/shell/bin/python

import os

path = '/root/bin'

for item in os.listdir(path):
    if item.endswith('.py'):
        _origin = os.path.join(path, item)
        _change = _origin.replace('.py', '')
        os.rename(_origin, _change)
        os.system(f"chmod +x {_change}")
        os.system(f"dos2unix {_change}")  # fix python ^M error
