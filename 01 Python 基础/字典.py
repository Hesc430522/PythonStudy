#字典的增删改查
'''
#创建字典
infor = {"name":"班长","age":18,"qq":861142965,"sex":"男"}
#创建列表
name_new = ['老王','老李','张三','李四']
#添加
infor ["addr"] = "12312321"

#删除
del infor["addr"]

#修改
infor['qq'] = 10086

#查询
print(infor.get('qq'))
'''
infor = {"name":"班长","age":18,"qq":861142965,"sex":"男"}
num = [11,22,33,44,55,66]
a = [1,2,3]
b = [4,5,6]
#while循环遍历列表
'''
num_lenght = len(num)
i = 0
while i<num_lenght:
    print(num[i])
    i+=1
'''

#for 循环遍历列表
'''
for temp in num:
   print(temp)
else:
    print("============")
'''

#列表的append-extend操作
'''
a.extend(b)
a.append(b)
print(a)
'''

#append 注意点
'''
#a = a.extend(b)
a = a.append(b)
print(a)
'''

#len的用发
print(len(infor))