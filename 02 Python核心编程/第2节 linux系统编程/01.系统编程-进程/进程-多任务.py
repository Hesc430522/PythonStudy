import os
import time


ret = os.fork()
# windows os 模块没有fork功能

if  ret == 1:
    while True:
        time.sleep(1)
        print("-------1-------",ret)
else:
    while True:
        time.sleep(1)
        print("-------2-------",ret)