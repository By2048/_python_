import time

from collections import deque

import pysnooper


# https://docs.python.org/zh-cn/3/library/collections.html

@pysnooper.snoop(watch_explode=('dq',))
def test():
    dq = deque([-1, 0])
    dq.append(1)
    dq.append([2, 3])
    dq.appendleft('a')
    return dq


test()
