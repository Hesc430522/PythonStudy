class Test:
    def __init__(self):
        self.num = 100
        self.__num2 = 200  # __私有属性，子类不能被继承
        self.__num = 100  # __私有属性

    def __test1(self):  # __私有方法，子类不能被继承
        print("----test1----")

    def test(self):  # 公共方法
        print("----test----")

    def test3(self):
        print("----test3----")
        self.__test1()
        print("test3:" + str(self.__num2))

    def setNum(self, Newnum):
        print("====SetNum====")
        self.__num = Newnum

    def getNum(self):
        print("====getNum====")
        return self.__num

    num = property(getNum, setNum)


t = Test()
# b = B()
# b.test3()
# b.b_test()
# print(b.num)

# 父类的私有属性不能被继承
# b.__test1
# print(b.__nume2)
t.num = 90
print(t.num)
