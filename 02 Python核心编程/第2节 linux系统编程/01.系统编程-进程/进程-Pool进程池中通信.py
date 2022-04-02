from multiprocessing import Manager,Pool
import time
import random
import os

def write(q):
    print("writer启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for value in "ABCDEFGHIJK":
        q.put(value)

def read(q):
    print("reader启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s" % q.get(True))


if __name__ == '__main__':
    q = Manager().Queue()
    po = Pool()
    po.apply(func=write, args=(q,))
    po.apply(func=read, args=(q,))
    po.close()
    po.join()

