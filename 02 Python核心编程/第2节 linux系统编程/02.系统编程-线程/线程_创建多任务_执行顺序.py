#coding=utf-8
import threading
import time
#进程执行顺序，主要看系统调度，不一定是主进程先走。
#线程执行顺序无序

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm" +self.name+'@'+ str(i) #name属性中保存的是当前线程的名字
            print(msg)

def test():
    for i in range(5):
        my = MyThread()
        my.start()


if __name__ == '__main__':
    test()




