# 使用fork创建子进程时，将主进程kill掉，等子进程运行完也会自动kill
# windows os 模块没有fork功能
# windows 使用from multiprocessing import Process 创建多进程

import os
import time

ret = os.fork()
# 每执行一次fork创建两个进程
if ret == 0:
    while True:
        print("----1----")
        time.sleep(1)
else:
    while True:
        print("----2----")
        time.sleep(1)

