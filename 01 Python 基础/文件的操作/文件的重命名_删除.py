import os

old_file_name = input("请输入你要更改的文件名称：")
#new_file_name = input("更改后的文件名称：")
#os.rename(old_file_name,new_file_name)
os.remove(old_file_name)