import time
from tqdm import *
# for i in tqdm(range(1000)):
#     time.sleep(0.01)    #进度条每0.1s前进一次，总时间为1000*0.1=100s

# text = ""
# for char in tqdm(["a", "b", "c", "d"]):
#     time.sleep(1)
#     text = text + char

# pbar = tqdm(total=100)
# for i in range(10):
#     time.sleep(1)
#     print('werwerwe')
#     time.sleep(1)
#     pbar.update(10)
# pbar.close()

from tqdm import trange
from random import random, randint
from time import sleep

t = trange(100)
for i in t:
    # Description will be displayed on the left
    t.set_description('GEN %i' % i)
    # Postfix will be displayed on the right, and will format automatically
    # based on argument's datatype
    t.set_postfix(loss=random(), gen=randint(1,999), str='h', lst=[1, 2])
    sleep(0.1)