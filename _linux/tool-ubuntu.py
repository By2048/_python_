#!/root/.pyenv/versions/shell/bin/python

import os

package = [
    'lrzsz',
    'dos2unix'
]

for item in package:
    os.system(f"apt install -y {item}")
