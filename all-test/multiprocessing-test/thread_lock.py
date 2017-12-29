"""
多线程和多进程最大的不同在于，
多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多线程中，所有变量都由所有线程共享，
所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时修改一个变量，把内容给改乱了。
"""

import time, threading

balance = 0
def change_it(n):
    # 先存后取，结果应该是0
    global balance
    balance = balance + n
    balance = balance - n
    print(balance)
"""
# 假定这是你银行的存款


def run_thread(n):
    for i in range(100000):
        change_it(n)

"""
"""
如果我们要确保balance计算正确，就要给change_it()上一把锁，
当某个线程开始执行change_it()时，
我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，
直到锁被释放后，获得该锁以后才能改。
由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，
所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：

当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，
然后继续执行代码，其他线程就继续等待直到获得锁为止。

锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行，
坏处当然也很多，首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，
效率就大大地下降了。
其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，
可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
"""

lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)



