encoding='UTF-8'
#open   打开
#close  关闭
#writ   新增
#read   读取

#以utf-8格式打开文件打开文件
f = open("test.txt","rb")
f_new = open("test附件.txt","wb")
#读取文件内容
string  = f.read()
f_new.write(string)

f_new.close()
f.close()




