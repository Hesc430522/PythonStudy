'''myStr = "何顺成，正在学习python。何顺成，正在学习python"
print(myStr)
print(myStr.find("学习"))
print(myStr.find("6"))
print(myStr.count("何"))
print(myStr.replace("python","python。",1))
print(myStr.split("，"))
print(myStr.center(50))
test =(myStr.center(50))
print(test.strip(" "))'''
names =['何顺成','何千辛','何也林']
names2 =['何顺成1','何千辛1','何也林1']
names.append("刘建新")
names.extend(names2)
print(names)
names.pop(-1)
print(names)
#names3 = names + names2
#print(names3.pop())
#print(names3)