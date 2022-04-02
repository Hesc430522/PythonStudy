#导入生成随机数包
import random

#定义函数
'''
def print_mp():
    print("-"*20)
    print("     名片管理系统V.0.1")
    print("-"*20)

def print_sjx():
    print("*")
    print("*"*2)
    print("*" * 3)
    print("*" * 4)
    print("*" * 5)
    print("*" * 6)
print_mp()
print_sjx()
'''

#定义带参数的函数
'''
def sum_2_nums(num1,num2):
    #a = 10
    #b = 20
    #定义随机数顺范围
    randoms = random.randint(1, 100)
    result = num1+num2
    results =(num1+num2)*randoms

    print("%d+%d=%d"%(num1,num2,result))
    print("(%d+%d)*%d=%d" % (num1, num2,randoms, results))
    return results
num1 = int(input("请输入第一个值："))
num2 = int(input("请输入第二个值："))

#调用函数
sum_2_nums(num1,num2)
'''

#带返回值的函数
'''
def age(num1):
    age_num= num1
    print("你输入的值是：%s"%age_num)
    return age_num

def cj():
    a = result * 3.1415926
    print(a)

num1 = int(input("请输入第一个值："))
result = age(num1)
cj()
'''

#带多个返回的函数
'''
def More():
    aa =11
    bb =22
    cc =33
    dd =[aa,bb,cc]
    return (dd)
i = More()
print(i[0],i[1],i[2])
'''

#4种函数的类型
'''
无参数，无返回值
无参数，有返回值
有参数，无返回值
有参数，有返回值
'''

#函数相互调用
'''
def test1():
    i = 0
    while i <5:
        print("--------1")
        i +=1

def test2():
    print("----------2")
    test1()
    print("----------2")

test2()
'''

#实例
age_new = 0
#实现和
def sum(a1,b2,c3):
    age_int = a+b+c
    return age_int

#实现平均值
def age(a,b,c):
    age_int = sum(a,b,c)
    global age_new
    age_new =age_int/3

    return age_new

#实现平均值的平方

def square(a,b,c):
    #square_int = age(a,b,c)
    square_int = age_new * age_new
    return square_int


a = int(input("请输入："))
b = int(input("请输入："))
c = int(input("请输入："))

sum_new = sum(a,b,c)
print("和为:",sum_new)

age_new = age(a,b,c)
print("平均值为:",age_new)

square_int = square(a,b,c)
print("平均值的平方为:",square_int)

