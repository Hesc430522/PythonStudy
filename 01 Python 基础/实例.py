import time

file_name = "users[附件].csv"
#print(file_name)
try:
    f = open(file_name,encoding='utf-8')
    try:
        while True:

            content = f.readline()
            #content = f.find("@qq.com")
            if  len(content) == 0:
                break
            else:
                time.sleep(1)
                print(content)
    except:
        pass

    finally:
        print("关闭文件！！")
        f.close()

except Exception:
    print("没有这个文件，你输入的文件名称有误")

