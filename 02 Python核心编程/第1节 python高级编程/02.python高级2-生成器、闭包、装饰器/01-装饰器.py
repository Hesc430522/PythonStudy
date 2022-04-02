# 装饰器
print("装饰器学习！")


def foo(func):
    print("foo函数")

    def inner():
        print("====正在验证====")
        func()

    return inner


@foo  # 语法糖
def f1():
    print("====F1====")

@foo
def f2():
    print("====F2====")


f1()
f2()
print("="*50 + "分隔符" + "="*50)

# 定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        print("----1---")
        return "<b>" + fn() + "</b>"
    return wrapped

# 定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        print("----2---")
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
@makeItalic
def test3():
    print("----3---")
    return "hello world-3"

ret = test3()
print(ret)
