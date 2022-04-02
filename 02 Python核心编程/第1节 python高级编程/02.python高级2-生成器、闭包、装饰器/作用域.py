# 1、什么是命名空间
# 比如有一个学校，有10个班级，在7班和8班中都有一个叫“小王”的同学，如果在学校的广播中呼叫“小王”时，7班和8班中的这2个人就纳闷了，你是喊谁呢！！！
# 如果是“7班的小王”的话，那么就很明确了，那么此时的7班就是小王所在的范围，即命名空间

# 2、LEGB 规则
# Python 使用 LEGB 的顺序来查找一个符号对应的对象
# locals -> enclosing function -> globals -> builtins
# locals：当前所在命名空间（如函数、模块），函数的参数也属于命名空间内的变量
# enclosing：外部嵌套函数的命名空间（闭包中常见）
# globals：全局变量，函数定义所在模块的命名空间
# builtins：内建模块的命名空间。

print("1、作用域")
number = 300
def fun1():
    number = 200

    def fun2():
        number = 100
        # a 位于外部嵌套函数的命名空间
        print(number)
    return fun2


ret = fun1()
ret()