class Base():
    def hello(self):
        print("hello world")

class a(Base):
    def test(self):
        print("你好")

class b(a,Base):
    def test1(self):
        print("空你几哇")

bb = b()
bb.test()
bb.test1()
bb.hello()