from multiprocessing import Process
import os

"""
    子进程要执行的代码
"""


def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))

# 启动一个子进程并等待其结束
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test_code',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')



