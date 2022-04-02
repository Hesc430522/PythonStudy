class Dog(object):
    def test1(self):
        print("大家好！！")


class xiao(object):
    def test1(self):
        print("你好！！")


def select(temp):
    temp.test1()
    print("%s.test1()" %'temp')


dog1 = Dog()
dog2 = xiao()
select(dog1)
select(dog2)
