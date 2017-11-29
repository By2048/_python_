import os
import functools

lk = r'E:\Desktop\NoteBook\Web\JavaScript\_code\Beginning JavaScript 5E downloads'


def my_cmp(item1, item2):
    len1 = len(item1)
    len2 = len(item2)
    if len1 > len2:
        return 1
    elif len1 < len2:
        return -1
    else:
        return 0


aa = [1, 2]
bb = [1, 2, 3]
cc = [1, 2]
dd = [1, 2, 3, 4]
ee = [1]

pp = [aa, bb, cc, dd, ee]

for p in pp:
    print(p)

pp.sort(key=functools.cmp_to_key(my_cmp))

for p in pp:
    print(p)