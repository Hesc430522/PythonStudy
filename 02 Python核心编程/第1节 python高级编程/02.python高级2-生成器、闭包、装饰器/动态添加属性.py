# 动态添加属性
# 动态编程语言 是 高级程序设计语言 的一个类别，在计算机科学领域已被广泛应用。
# 它是一类 在运行时可以改变其结构的语言 ：例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化。动态语言目前非常具有活力。
# 例如JavaScript便是一个动态语言，除此之外如 PHP 、 Ruby 、 Python 等也都属于动态语言，而 C 、 C++ 等语言则不属于动态语言。----来自 维基百科

import types

# 1、运行的过程中给对象绑定(添加)属性
print("1、运行的过程中给对象绑定(添加)属性")


class Person1(object):
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


P = Person1("小明", "24")  # 创建人的对象类，添加name和age属性
P.sex = "男"  # 新添加sex对象属性，保存人的性别
print("姓名：%s  年龄：%s  性别：%s\n" % (P.name, P.age, P.sex))  # 打印

# 2. 运行的过程中给类绑定(添加)属性
print("2. 运行的过程中给类绑定(添加)属性")

P1 = Person1("崽崽", "25")
Person1.sex = "女"  # 给类Person1添加sex属性
print("姓名：%s  年龄：%s  性别：%s\n" % (P1.name, P1.age, P1.sex))  # 打印

# 3、运行的过程中给类绑定(添加)方法
print("3、运行的过程中给类绑定(添加)方法")


class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name


def run(self):
    print("%s正在奔跑！" % self.name)


p1 = Person(20, "p1")
p1.run = types.MethodType(run, p1)  # 给这个对象添加实例方法

p1.run()
print(p1.name)
print(p1.age)


# 4、使用__slots__限制class 添加属性
class Person(object):
    __slots__ = ("name", "age")


P = Person()
P.name = "老王"
P.age = 20
P.score = 100

"""
Traceback (most recent call last):
  File "F:\Code\Python\Python 学习代码\\02 Python核心编程\第2节 python高级2-生成器、闭包、装饰器\动态添加属性.py", line 59, in <module>
    P.score = 100
AttributeError: 'Person' object has no attribute 'score'

"""
