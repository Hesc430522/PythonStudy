class Cat:
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age
        #print("*************新年快乐*************")
    def __str__(self):
        return print("%s的年龄是：%d"%(self.name,self.age))

    def eat(self):

        print("吃鱼！！！")

    def drink(self):

        print("喝可乐！！")
    def export(self):
        print("%s的年龄是：%d"%(self.name,self.age))

tom = Cat("汤姆",40)

lma = Cat("蓝猫",10)


print(tom)

print(lma)



