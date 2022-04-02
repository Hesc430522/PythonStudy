'''a = 30
if a > 0 and a<= 50:
  print("a在0到50之间！")'''

''''
#if条件
1.
if 条件：
  print

2.  
if 条件:
  print("")
else:
  print("")

3.
if 条件1
  print("")
elif 条件2:
  print("")
elif 条件3:
  print("") '''

#判断性别
sex = input("请输入你的性别：")
if sex == "男":
  print("你是大老爷们！")
elif sex == "女":
  print("你是女生！")
elif not (sex == "男" and sex == "女"):
    print("请输入正确性别：")


num = int(input ("请输如一个数字（1-7）："))

if num == 1:
  print("星期一")
elif num ==2:
  print ("星期二")
elif num ==3:
  print ("星期三")
elif num ==4:
  print ("星期四")
elif num ==5:
  print ("星期五")
elif num ==6:
  print ("星期六")
elif num ==7:
  print ("星期日")

