# -*- coding: cp936 -*-
#输入姓名
#输入性别
#输入年龄

name = input("请输入你的姓名：")
xb = input("请输入你的性别：")
age = input("请输入你的年龄：")
#input 默认输入的是字符串类型
csrq =input("请输入你的出生日期：")
age_nmu = int(age)
print("="*20)
print("姓名是：%s,性别是：%s,年龄是：%d,出生日期是：%s"%(name,xb,age_nmu,csrq))
print("="*20)
