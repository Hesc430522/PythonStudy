print("multiprocessing.Pool常用函数解析")
# multiprocessing.Pool常用函数解析
# apply_async(func[, args[, kwds]]) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），args为传递给func的参数列表，kwds为传递给func的关键字参数列表；
# apply(func[, args[, kwds]])：使用阻塞方式调用func
# close()：关闭Pool，使其不再接受新的任务；
# terminate()：不管任务是否完成，立即终止；
# join()：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；


from multiprocessing import Pool
import os
import random
import time

def worker(num):
    for i in range(random.randint(1, 5)):
        print("====pid=%d===num=%d===="%(os.getpid(),num))
        time.sleep(1)

if __name__ == '__main__':
    #3表示进程池最多同时运行3个进程数
    pool = Pool(3)
    for i in range(10):
        print("---%d----"%i)
        pool.apply_async(worker,(i,))
        # pool.apply(worker, (i,))  # 堵塞式添加任务
    pool.close()
    pool.join()

# 栈：先进后出
# 队列： 先进先出