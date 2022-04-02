# 1、闭包
def test(number):
    print("=" * number)
    print(number)

    def test_in(number_in):
        print("=" * number_in)
        return number * number_in

    return test_in


ret = test(100)  # 传递参数100给test函数的number并返回test_in函数引用地址给ret -> test_in
print(ret(5))  # 给ret -> test_in(100)传递100，test_in 函数返回 number*number_in 的值
print("="*50+"分割符" + "="*50)


def line_conf(a, b):  # 2、闭包应用
    def line(x):
        return a*x + b
    return line


line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5))
print(line2(5))
