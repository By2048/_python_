import time, threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)



"""
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，
主线程又可以启动新的线程，
Python的threading模块有个current_thread()函数，它永远返回当前的线程的实例。
主线程实例的名字叫MainThread，子线程的名字创建时指定，
我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，
如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
"""