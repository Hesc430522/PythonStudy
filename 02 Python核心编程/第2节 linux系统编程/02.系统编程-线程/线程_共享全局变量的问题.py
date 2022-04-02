from threading import Thread,Lock

# 多线程同时进行操作需要加锁
num=0
def work():
    global num
    for i in range(1000000):
        lock.acquire()
        num += 1
        lock.release()
    print("workg_num的值%d"%num)

def work1():
    global num
    for i in range(1000000):
        lock.acquire()
        num += 1
        lock.release() # 添加lock.release() 方法解决
    print("work1g_num的值%d"%num)


lock = Lock()

t1 = Thread(target=work)
t1.start()


t2 = Thread(target=work1)
t2.start()

print("num的值为：%d"%num)