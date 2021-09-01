import time
import threading

threading_local = threading.local()

"""

threading.local()这个方法的特点用来保存一个全局变量，但是这个全局变量只有在当前线程才能访问，

localVal.val = name这条语句可以储存一个变量到当前线程，如果在另外一个线程里面再次对localVal.val进行赋值，

那么会在另外一个线程单独创建内存空间来存储，也就是说在不同的线程里面赋值 不会覆盖之前的值，因为每个

线程里面都有一个单独的空间来保存这个数据,而且这个数据是隔离的，其他线程无法访问



这个东西可以用在那些地方呢，比如下载，现在都是多线程下载了，就像酷狗那样，可以同时下载很多首歌曲，那么

就可以利用这个方法来保存每个下载线程的数据，比如下载进度，下载速度之类的



所以  如果你在开发多线程应用的时候  需要每个线程保存一个单独的数据供当前线程操作，可以考虑使用这个方法，简单有效

其实这样的功能还有很多种方法可以实现，比如我们在主线程实例化一个dict对象，然后用线程的名字作为key，因为线程之间可以共享数据，

所以也可以实现相同功能，并且灵活性更多，不过代码就没那么优雅简洁了
"""


def test_3():
    def print_data():
        data = threading_local.data
        print(f'{data} in {threading.current_thread().name}')

    def target(name):
        threading_local.data = name
        print_data()

    thread_a = threading.Thread(target=target, args=('AAA',), name='ThreadA')
    thread_b = threading.Thread(target=target, args=('BBB',), name='ThreadB')

    thread_a.start()
    thread_b.start()

    thread_a.join()
    thread_b.join()


value_global = 0

value_local = threading.local()


def test1():
    def run(arg):
        global value_global
        value_global = arg
        time.sleep(2)
        print(value_global)

    for i in range(10):
        thread = threading.Thread(target=run, args=(i,))
        thread.start()


def test2():
    def run(arg):
        value_local.value = arg
        time.sleep(2)
        print(value_local.value)

    for i in range(10):
        thread = threading.Thread(target=run, args=(i,))
        thread.start()


if __name__ == '__main__':
    test1()
    test2()
