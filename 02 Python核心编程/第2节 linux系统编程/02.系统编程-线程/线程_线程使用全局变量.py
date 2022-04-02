from threading import Thread
import time

#线程与线程共享全局变量

num = 0

def work1():
    global num
    for l in range(10000000):
        num += 1

    print("--修改num为103--num woek1, num is %d"%num)

def work2():
    global num
    print("--取num的值--num woek2, num is %d" % num)

print("-----线程没创建之前num值为%d"%num)

t1=Thread(target=work1)
t1.start()
#time.sleep(1) 屏蔽

t2 =Thread(target=work2)
t2.start()
