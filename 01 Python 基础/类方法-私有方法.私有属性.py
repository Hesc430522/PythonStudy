class A:
    def __init__(self):
        self.num = 100
        # __私有属性，子类不能被继承
        self.__num2 = 200

    def test(self):
        print("---test---")
    # __表示私有方法，子类不能被继承
    def __test1(self):
        print("---test1---")

    def test3(self):
        self.__test1()
        print(self.__num2)

class B(A):
    pass

b = B()
print(b.num)
# 父类的私有属性不能被继承
# print(b.__num)
b.test()
b.test3()
# 父类的私有方法不能被继承
# b.__test()
