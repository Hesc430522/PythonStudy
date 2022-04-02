class Test(object):
    def __init__(self):
        self.__num = 100
        #私有属性
    def setnum (self,num):
        self.__num = num

    def getnum(self):
        return self.__num
    num = property(getnum,setnum)

t =Test()
print(t.num)#相当于调用getnum方法
t.num = 50#相当于调用setnum方法
print (t.num)


