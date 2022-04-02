import os
import time

g_num = 100

ret = os.fork()
if ret > 0:
    g_num+=1
    print("父进程的g_num的值为:%d"%g_num)
else:
    print("子进程的g_num的值为:%d" % g_num)
