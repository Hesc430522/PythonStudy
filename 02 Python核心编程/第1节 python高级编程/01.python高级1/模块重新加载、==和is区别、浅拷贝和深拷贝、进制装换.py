import a
import sys
# from imp import *  # 3.3 版本弃用
from importlib import *
# ==和is的区别
import copy
# 1、import导包问题
print("1、import导包问题")
# Python 默认导入包路径是从sys.path变量依次向下(↓)搜索导入,缺少导入包的路径可以使用sys.path.append() 方法添加
# F:\Code\Python\Python 学习代码\02 Python核心编程\01.python高级1
# F:\Code\Python\Python 学习代码
# D:\Application\JetBrains\PyCharm 2020.3.3\plugins\python\helpers\pycharm_display
# D:\Application\Python\Python39\python39.zip
# D:\Application\Python\Python39\DLLs
# D:\Application\Python\Python39\lib
# D:\Application\Python\Python39
# D:\Application\Python\Python39\lib\site-packages
# D:\Application\JetBrains\PyCharm 2020.3.3\plugins\python\helpers\pycharm_matplotlib_backend

for path in sys.path:
    print(path)

# 使用append() 添加路径
sys.path.append("F:\Python\Python就业班\\02Python核心编程")

for path in sys.path:
    print(path)

# F:\Code\Python\Python 学习代码\02 Python核心编程\01.python高级1
# F:\Code\Python\Python 学习代码
# D:\Application\JetBrains\PyCharm 2020.3.3\plugins\python\helpers\pycharm_display
# D:\Application\Python\Python39\python39.zip
# D:\Application\Python\Python39\DLLs
# D:\Application\Python\Python39\lib
# D:\Application\Python\Python39
# D:\Application\Python\Python39\lib\site-packages
# D:\Application\JetBrains\PyCharm 2020.3.3\plugins\python\helpers\pycharm_matplotlib_backend
# F:\Python\Python就业班\02Python核心编程

# 2、重新加载import模块
print("2、重新加载import模块")
# 当 import 模块发生更改时可以使用reload()重新加载模块,需要导入imp模块：from imp import * --3.3 版本已弃用 使用importlib 方法
a.a("你好！")
reload(a)

# 3、is 和 ==区别
print("3、is 和 ==区别")
# is 是比较两个引用是否指向了同一个对象（引用比较）
# == 是比较两个对象是否相等。

a = [11, 22, 33, 44, 55]
b = a  # 将引用地址指定给b

c = copy.deepcopy(a)
if a is b:
    print("True")
    print(id(a))
    print(id(b))

if a == b:
    print("True")
    print(id(a))
    print(id(b))
else:
    print("False")

if a is c:
    print("True")
    print(id(a))
    print(id(c))
else:
    print("False")
    print(id(a))
    print(id(c))

if a == c:
    print("True")
    print(id(a))
    print(id(c))
else:
    print("False")
    print(id(a))
    print(id(c))

# 4、浅拷贝和深拷贝
print("4、浅拷贝和深拷贝")
# 浅拷贝
# 浅拷贝是对于一个对象的顶层拷贝
# 通俗的理解是：拷贝了引用，并没有拷贝内容
a = [11, 22, 33]
b = a  # 浅拷贝

# 深拷贝
# 深拷贝是对于一个对象所有层次的拷贝(递归)
c = copy.deepcopy(a)  # 深拷贝

# 5、进制转换
print("5、进制转换")
# 二进制 -> 十进制：int("0b10010",2)
# 八进制 -> 十进制：int("0x12",16)
# 十六进制 -> 十进制：int("0o22",8)

# 十进制 -> 二进制：bin(18)
# 十进制 -> 八进制：oct(18)
# 十进制 -> 十六进制：hex(18)

print("二进制：" + bin(18))
print("八进制：" + oct(18))
print("十六进制：" + hex(18))

print("二进制转十进制：" + str(int(bin(18), 2)))
print("八进制转十进制：" + str(int(oct(18), 8)))
print("十六进制转十进制：" + str(int(hex(18), 16)))







