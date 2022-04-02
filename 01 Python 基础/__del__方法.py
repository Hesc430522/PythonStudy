import sys
class Dog:
    def __del__(self):
        print("---游戏结束---")

class T():
    pass

dog1 = Dog()
dog2 = dog1
del dog1
del dog2
print(45*475+3125)

t=T()
tt = t
#查看一个对象的引用计数的方式
print(sys.getrefcount(t))
