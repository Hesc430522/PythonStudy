encoding='UTF-8'

old_file_name = input("请输入你要复制的文件名：")#获取文件名称

print()

old_file = open(old_file_name,"rb") #打开文件

location_num = old_file_name.find(".")

#新的文件名称
new_file_name = old_file_name[:location_num]+"[附件]"+old_file_name[location_num:]

#old_file_name.rfind()

#创建新的文件
new_file = open(new_file_name,"wb")

#循环读取文件内容
while True:
    #读取文件内容#
    content = old_file.read(1024*1024*2)

    if len(content) == 0:
        break

    # 将文件的内容写入到新文件中
    new_file.write(content)




#关闭文件
old_file.close()
new_file.close()
