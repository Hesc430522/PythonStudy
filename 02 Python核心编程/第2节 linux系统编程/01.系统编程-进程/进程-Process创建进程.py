from multiprocessing import Process
# Process会先等子进程任务全部结束才会结束任务进程。
import time
import os

def test():
    while True:
        print("当前pid为：" + str(os.getpid()) + " 父进程pid为：" + str(os.getppid()))
        print("----2----")
        time.sleep(1)

if __name__ == '__main__':
    p = Process(target=test)
    p.start()  # 让这个进程开始执行test()函数代码
    while True:
        print("当前父进程pid为："+ str(os.getpid()))
        print("----1----")
        time.sleep(1)

