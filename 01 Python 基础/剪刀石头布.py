
import random

i=1
j=0
j =int(input("请输入你要玩的次数："))
while i ==i:
  if i>j:
    break
  wj =int(input("请输入你的值 剪刀0 石头1 布2:"))
  #print(i,j)
  dn = random.randint(0,2)
#赢了
  if (wj ==0 and dn ==2) or (wj ==1 and  dn ==0) or (wj ==2 and dn ==1):
    print("你赢了！")
    i+=1
    if dn ==0:
      print("电脑出的是剪刀!")
    elif dn==1:
      print("电脑出的是石头!")
    else:
      print("电脑出的是布!")
#平局
  elif wj==dn:
    i+=1
    print("平局！！！！！")
    if dn ==0:
      print("电脑出的是剪刀!")
    elif dn==1:
      print("电脑出的是石头!")
    else:
      print("电脑出的是布!")
#输了
  else :
    i+=1
    print("你输了！")
    if dn ==0:
      print("电脑出的是剪刀!")
    elif dn==1:
      print("电脑出的是石头!")
    else:
      print("电脑出的是布!")
            

