from multiprocessing import Pool,Manager
import os
import time

def copyFile(copyPath, newPath, name,q):
    fr = open(copyPath+"/"+name, "rb")    # 打开历史文件
    fw = open(newPath+"/"+name, "wb") # 打开新文件
    content = fr.read() # 读取文件
    fw.write(content)   # 写入数据到历史文件中
    fr.close() # 关闭文件
    fw.close() # 关闭文件
    q.put(name)

def process_bar(percent, start_str='', end_str='', total_length=0):
    bar = ''.join(["\033[31m%s\033[0m"%'   '] * int(percent * total_length)) + ''
    bar = '\r' + start_str + bar.ljust(total_length) + ' {:0>4.1f}%|'.format(percent*100) + end_str
    print(bar, end='', flush=True)

def main():
    num = 0 #初始化copy控制变量
    # copyPath = input("请输入你需要拷贝的文件夹路径:")
    copyPath = "E:\\Python\\视频\\课件和资料\\Python核心编程\\系统编程\\html版\\系统编程-完整课件\\02day"
    newPath = copyPath + "-复件"  # 需要创建新的文件夹
    if os.path.exists(newPath):
        print("Error:%s此文件夹已存在！" %newPath)
    else:
        os.mkdir(newPath)   # 创建新的文件夹
        print("INFO:已创建%s文件夹！" %newPath)

    copyFileName = (os.listdir(copyPath))  # 获取当前文件夹中的文件名称

    pool = Pool(5)  #使用多进程拷贝文件，设置进程池为5
    queue = Manager().Queue()

    for temp in copyFileName:
        pool.apply_async(func=copyFile, args=(copyPath, newPath, temp, queue))

    allNum = len(copyFileName)
    while num < allNum:
        queue.get()
        num += 1
        CopyRate = num/allNum
        print("\r复制进度：%.2f%%" %(CopyRate*100), end='', flush=True)
        time.sleep(0.1)

    print("\nINFO:拷贝文件结束！")

if __name__ == '__main__':
    main()


