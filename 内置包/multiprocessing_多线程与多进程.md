## 相关图书
[Python并行编程 中文版](http://python-parallel-programmning-cookbook.readthedocs.io/zh_CN/latest/)

## 多线程介绍
- 启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务。
- 启动一个进程，在一个进程内启动多个线程，多个线程也一块执行多个任务。
- 启动多个进程，每个进程再启动多个线程

线程并不是始终保持一个状态的，其状态大概如下：

- New 创建
- Runnable 就绪。等待调度
- Running 运行
Blocked 阻塞。阻塞可能在 Wait Locked Sleeping
Dead 消亡

线程有着不同的状态，也有不同的类型。大致可分为：

主线程
子线程
守护线程（后台线程）
前台线程


## 主线程结束后，子线程还在运行。
```py
import time
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)

def main():
    print("Start main threading")
    threads = [MyThread() for i in range(3)]
    for item in threads:
        item.start()
    print("End Main threading")

if __name__ == '__main__':
    main()

# Start main threading
# thread Thread-1, @number: 0
# thread Thread-2, @number: 0
# thread Thread-3, @number: 0
# End Main threading
# thread Thread-3, @number: 1
# thread Thread-2, @number: 1
# thread Thread-1, @number: 1
# thread Thread-3, @number: 2
# thread Thread-2, @number: 2
# thread Thread-1, @number: 2
# thread Thread-1, @number: 3
# thread Thread-3, @number: 3
# thread Thread-2, @number: 3
# thread Thread-1, @number: 4
# thread Thread-3, @number: 4
# thread Thread-2, @number: 4
```

## 主线程要等待子线程运行完后，再退出
```py
import time
import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print('thread {}, @number: {}'.format(self.name, i))
            time.sleep(1)

def main():
    print("Start main threading")
    threads=[MyThread() for i in range(3)]
    for item in threads:
        item.start()
    for item in threads:
        item.join()
    print("End Main threading")

if __name__ == '__main__':
    main()

# Start main threading
# thread Thread-1, @number: 0
# thread Thread-2, @number: 0
# thread Thread-3, @number: 0
# thread Thread-2, @number: 1
# thread Thread-3, @number: 1
# thread Thread-1, @number: 1
# thread Thread-1, @number: 2
# thread Thread-2, @number: 2
# thread Thread-3, @number: 2
# thread Thread-1, @number: 3
# thread Thread-3, @number: 3
# thread Thread-2, @number: 3
# thread Thread-3, @number: 4
# thread Thread-2, @number: 4
# thread Thread-1, @number: 4
# End Main threading
```


## 线程同步与互斥锁

使用线程加载获取数据，通常都会造成数据不同步的情况。可以给资源进行加锁，
`其中 `threading` 模块给我们提供了一个 Lock 功能。
``lock = threading.Lock()`
在线程中获取锁`lock.acquire()`
使用完成后，我们肯定需要释放锁`lock.release()`
当然为了支持在同一线程中多次请求同一资源，Python 提供了`可重入锁（RLock）`。RLock 内部维护着一个 Lock 和一个 counter 变量，counter 记录了 acquire 的次数，从而使得资源可以被多次 require。直到一个线程所有的 acquire 都被 release，其他的线程才能获得资源。
那么怎么创建重入锁`r_lock = threading.RLock()`

## Condition 条件变量

实用锁可以达到线程同步，但是在更复杂的环境，需要针对锁进行一些条件判断。Python 提供了 Condition 对象。使用 Condition 对象可以在某些事件触发或者达到特定的条件后才处理数据，Condition 除了具有 Lock 对象的 acquire 方法和 release 方法外，还提供了 wait 和 notify 方法。线程首先 acquire 一个条件变量锁。如果条件不足，则该线程 wait，如果满足就执行线程，甚至可以 notify 其他线程。其他处于 wait 状态的线程接到通知后会重新判断条件。
其中条件变量可以看成不同的线程先后 acquire 获得锁，如果不满足条件，可以理解为被扔到一个（ Lock 或 RLock ）的 waiting 池。直达其他线程 notify 之后再重新判断条件。不断的重复这一过程，从而解决复杂的同步


### 生产者消费者模式
```py
import threading, time

class Consumer(threading.Thread):
    def __init__(self, cond, name):
        # 初始化
        super(Consumer, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        print(self.name + ': 我这两件商品一起买，可以便宜点吗')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 我已经提交订单了，你修改下价格')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 收到，我支付成功了')
        self.cond.notify()
        self.cond.release()
        print(self.name + ': 等待收货')

class Producer(threading.Thread):
    def __init__(self, cond, name):
        super(Producer, self).__init__()
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        # 释放对琐的占用，同时线程挂起在这里，直到被 notify 并重新占有琐。
        self.cond.wait()
        print(self.name + ': 可以的，你提交订单吧')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 好了，已经修改了')
        self.cond.notify()
        self.cond.wait()
        print(self.name + ': 嗯，收款成功，马上给你发货')
        self.cond.release()
        print(self.name + ': 发货商品')

cond = threading.Condition()
producer = Producer(cond, '卖家 -->')
consumer = Consumer(cond, '买家 <--')
producer.start()
consumer.start()

# 买家 <--: 我这两件商品一起买，可以便宜点吗
# 卖家 -->: 可以的，你提交订单吧
# 买家 <--: 我已经提交订单了，你修改下价格
# 卖家 -->: 好了，已经修改了
# 买家 <--: 收到，我支付成功了
# 买家 <--: 等待收货
# 卖家 -->: 嗯，收款成功，马上给你发货
# 卖家 -->: 发货商品
```

## 线程通信
从一个线程向另一个线程发送数据最安全的方式可能就是使用 `queue` 库中的队列了。创建一个被多个线程共享的 `Queue` 对象，这些线程通过使用 `put()` 和` get()` 操作来向队列中添加或者删除元素。


```py
from queue import Queue
from threading import Thread

def write(values):
    # 写数据进程
    for i in range(10):
        value = '写进 <-- {0}'.format('val_' + str(i))
        print(value)
        values.put(value)

def read(values):
    # 读取数据进程
    while True:
        value = values.get(True)
        print('读取的值为 --> {0}'.format(value))

if __name__ == '__main__':
    values = Queue()
    t1 = Thread(target=write, args=(values,))
    t2 = Thread(target=read, args=(values,))
    t1.start()
    t2.start()

# 写进 <-- val_0
# 写进 <-- val_1
# 读取的值为 --> 写进 <-- val_0
# 写进 <-- val_2
# 读取的值为 --> 写进 <-- val_1
# 写进 <-- val_3
# 读取的值为 --> 写进 <-- val_2
# 写进 <-- val_4
# 写进 <-- val_5
# 读取的值为 --> 写进 <-- val_3
# 写进 <-- val_6
# 读取的值为 --> 写进 <-- val_4
# 写进 <-- val_7
# 读取的值为 --> 写进 <-- val_5
# 写进 <-- val_8
# 读取的值为 --> 写进 <-- val_6
# 写进 <-- val_9
# 读取的值为 --> 写进 <-- val_7
# 读取的值为 --> 写进 <-- val_8
# 读取的值为 --> 写进 <-- val_9
```

默认情况下，主线程退出之后，即使子线程没有 join。那么主线程结束后，子线程也依然会继续执行。如果希望主线程退出后，其子线程也退出而不再执行，则需要设置子线程为后台线程。Python 提供了 setDeamon 方法。


## 多进程
```py
import multiprocessing
import time


def worker(interval, name):
    print(name + ' start')
    time.sleep(interval)
    print(name + ' end')


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker, args=(1, '1'))
    p2 = multiprocessing.Process(target=worker, args=(2, '2'))
    p3 = multiprocessing.Process(target=worker, args=(3, '3'))

    p1.start()
    p2.start()
    p3.start()

    print("CPU number " + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print('name -> {0} \t pid -> {1}'.format(p.name,p.pid))
    print("end main")
# CPU number 4
# name -> Process-2 	 pid -> 16256
# name -> Process-1 	 pid -> 4448
# name -> Process-3 	 pid -> 17540
# end main
# 1 start
# 2 start
# 3 start
# 1 end
# 2 end
# 3 end
```

```py
import multiprocessing
import time


class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("当前时间: {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1


if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()

# 当前时间: Sun Apr  1 20:54:26 2018
# 当前时间: Sun Apr  1 20:54:29 2018
# 当前时间: Sun Apr  1 20:54:32 2018
# 当前时间: Sun Apr  1 20:54:35 2018
# 当前时间: Sun Apr  1 20:54:38 2018
```

## daemon
如果在子进程中添加了 daemon 属性，那么当主进程结束的时候，子进程也会跟着结束。所以没有打印子进程的信息。


### 没有加 deamon 属性的例子：
```py
# -*- coding: UTF-8 -*-
import multiprocessing
import time


def worker(interval):
    print('工作开始时间：{0}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.ctime()))


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))
    p.start()
    print('end')

# end
# 工作开始时间：Sun Apr  1 20:58:53 2018
# 工作结果时间：Sun Apr  1 20:58:56 2018
```

### 在上面示例中，进程 p 添加 daemon 属性：
```py
# -*- coding: UTF-8 -*-

import multiprocessing
import time


def worker(interval):
    print('工作开始时间：{0}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.ctime()))


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))
    p.daemon = True
    p.start()
    print('end')

# end
```


## join 
线程被创建之后并不会马上运行，需要手动调用 start() ， join() 让调用它的线程一直等待直到执行结束（即阻塞调用它的主线程， t 线程执行结束，主线程才会继续执行）：

join 方法的主要作用是：阻塞当前进程，直到调用 join 方法的那个进程执行完，再继续执行当前进程。
因此看下加了 join 方法的例子：

```py
import multiprocessing
import time

def worker(interval):
    print('工作开始时间：{0}'.format(time.ctime()))
    time.sleep(interval)
    print('工作结果时间：{0}'.format(time.ctime()))


if __name__ == '__main__':
    p = multiprocessing.Process(target=worker, args=(3,))
    p.daemon = True
    p.start()
    p.join()
    print('end')
# 工作开始时间：Sun Apr  1 20:59:51 2018
# 工作结果时间：Sun Apr  1 20:59:54 2018
# end
```
## pool
进程池的方法批量创建子进程。
```py
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('进程的名称：{0} ；进程的PID: {1} '.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('进程 {0} 运行了 {1} 秒'.format(name, (end - start)))


if __name__ == '__main__':
    print('主进程的 PID：{0}'.format(os.getpid()))
    p = Pool(4)
    for i in range(6):
        p.apply_async(long_time_task, args=(i,))
    p.close()
    # 等待所有子进程结束后在关闭主进程
    p.join()
    print('end')

# 主进程的 PID：8288
# 进程的名称：0 ；进程的PID: 2512 
# 进程的名称：1 ；进程的PID: 108 
# 进程的名称：2 ；进程的PID: 16148 
# 进程的名称：3 ；进程的PID: 14856 
# 进程 3 运行了 0.689537763595581 秒
# 进程的名称：4 ；进程的PID: 14856 
# 进程 1 运行了 1.7992887496948242 秒
# 进程的名称：5 ；进程的PID: 108 
# 进程 4 运行了 1.517038106918335 秒
# 进程 0 运行了 2.328686237335205 秒
# 进程 2 运行了 2.4697487354278564 秒
# 进程 5 运行了 1.311915397644043 秒
# end
```
 Pool 对象调用 join() 方法会等待所有子进程执行完毕，调用 join() 之前必须先调用 close() ，调用close() 之后就不能继续添加新的 Process 了。


 ## 进程之间通信
 ```py
 from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('写进程的PID:{0}'.format(os.getpid()))
    for value in ['val_1', 'val_2', 'val_3']:
        print('写进 Queue 的值为：{0}'.format(value))
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('读进程的PID:{0}'.format(os.getpid()))
    while True:
        value = q.get(True)
        print('从 Queue 读取的值为：{0}'.format(value))

if __name__ == '__main__':
    # 父进程创建 Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    # pr 进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()

# 
# 写进程的PID:17596
# 写进 Queue 的值为：val_1
# 读进程的PID:3848
# 从 Queue 读取的值为：val_1
# 写进 Queue 的值为：val_2
# 从 Queue 读取的值为：val_2
# 写进 Queue 的值为：val_3
# 从 Queue 读取的值为：val_3
 ```


 ## lock
多线程中加锁与不加锁区别
 ```py
import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
COUNT = 100000
shared_resource_lock = threading.Lock()


# 有锁的情况
def increment_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()


def decrement_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()


# 没有锁的情况
def increment_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock += 1


def decrement_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock -= 1


if __name__ == "__main__":
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("the value of shared variable with lock management is %s" % shared_resource_with_lock)
    print("the value of shared variable with race condition is %s" % shared_resource_with_no_lock)

# the value of shared variable with lock management is 0
# the value of shared variable with race condition is -23414

 ```