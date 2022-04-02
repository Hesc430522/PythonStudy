#coding=utf-8
import threading
import time

class MyThread(threading.Thread): # 调用threading.Thread为父类，继承threading.Thread父类的属性和方法
    def run(self):
        for i in range(10):
            time.sleep(1)
            msg = "I'm "+self.name+' @ '+str(i) #name属性中保存的是当前线程的名字
            print(msg)


if __name__ == '__main__':
    t = MyThread()  # 创建t的MyThread()对象
    t.start()   # 启动start方法