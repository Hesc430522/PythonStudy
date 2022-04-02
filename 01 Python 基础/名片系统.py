#1.打印功能列表
print("*"*20)
print("1.新增一个名字")
print("2.修改一个名字")
print("3.删除一个名字")
print("3.查询一个名字")
print("名片关系系统V8.6")
print("*"*20)
names =[]
while True:
  i =   int(input("请输入的你要操作的字符:"))
  if i == 1:
      print("请输入你要新增的名字：")
  elif i == 2:
      print("请输入你要修改的名字：")
  elif i == 3:
      print("请输入你要删除的名字：")
