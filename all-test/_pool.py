import multiprocessing
from  multiprocessing import *

def fun(num):
    nums=[]
    i=0
    while i<=num:
        nums.append(i)
        i+=1
    # print (nums)
    return nums
def run(num):
    return num*2


if __name__ == '__main__':
    # pool = multiprocessing.Pool(5)
    # list=[]
    # tmp=[]
    # tmp.append(pool.apply_async(function,(0,)))
    # # tmp.start()
    # for i in tmp:
    #     for j in i.get():
    #         print (j)

    pool=multiprocessing.Pool(4)
    max=4
    count=1
    out=[]
    while(count<=max):
        out.append(pool.apply_async(run,(count,)))
        count+=1
    print(out)
    pool.close()
    pool.join()
    for tmp in out:
        print(tmp.get())