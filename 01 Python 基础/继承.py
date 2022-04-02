class Auimal:
    def eat(self):
        print("===调用基类===")
    def edrink(self):
        print("===喝===")
    def sleep(self):
        print("===睡觉===")
    def run(self):
        print("===跑===")
class Dog(Auimal):
    def bark(self):
        print("===调用父类===")

class Xiaotq(Dog):
    def fei(self):
        print("===腾云驾雾===")
    def bark(self):
        print("===调用自己方法重写====")

        #第1种调用被重写的父类方法
        #Dog.bark(self)

        #第二种
        super().bark()
xiaotq = Xiaotq()
xiaotq.fei()
xiaotq.bark()
xiaotq.eat()
