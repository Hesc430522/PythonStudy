#全局变量，局部变量
'''
a = 100
#全局变量

def test():
    print(a)

def test1():
    #修改全部变量时要加global  a
    global  a
    a = 200
    #局部变量
    print(a)

test()
test1()'''

#不定长数参数
'''
def nums(a,b,c=33,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    print("*" * 20)
    
    result = a+b
    print(result)
    for num in args:
        result += num
    print("result=%d"%result)
    
a = [11,22,33]
b = {'name':"何顺成",'sex':"男"}
#元组的拆包，字典的拆包
nums(11,22,0,44,55,66,77,88,name="何顺成",xb="男")
nums(11,22,*a,**b)
#nums(11,22,33)
#nums(11,22,)
'''

#递归
'''
def getnum(num):
    if num >1:
        return num * getnum(num-1)
    else:
        return num

    #print(num)

result = getnum(4)
print(result)
'''
#递归死循环
'''
def nums():
    print("哈哈")
    nums()

nums()
'''

#匿名函数
'''
def test(a,b,func):
    result = func(a,b)
    return result

#func_new =eval(input("输入匿名函数："))
func_new = input("输入匿名函数：")
#在python3里面input是用字符串存储

#用eval 装换成正值类型
func_new = eval(func_new)

#lambda x,y:x+y

num = test(11,22,func_new)
print(num)
'''

#交换变量
'''
a = 44
b = 55
print("a=%d,b=%d"%(a,b))
a,b = b,a
print("a=%d,b=%d"%(a,b))
'''

#变量装换

