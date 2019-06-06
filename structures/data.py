import random
import time

MAX_LEN = 100_000
MAX_RANDOM = 100_000
MAX_SEARCH = 3_000

_list = []
_set = set()
_dict = dict()

for i in range(0, MAX_LEN):
    item = random.randint(0, MAX_RANDOM)
    _list.append(item)
    _set.add(item)
    _dict[i] = item

start = time.time()
for i in range(MAX_SEARCH):
    _ = i in _set
end = time.time()
print(" set:", end - start)

start = time.time()
for i in range(MAX_SEARCH):
    _ = i in _dict
end = time.time()
print("dict:", end - start)

start = time.time()
for i in range(MAX_SEARCH):
    _ = i in _list
end = time.time()
print("list:", end - start)
