class Dog(object):
    __instance = None
    __inst_fiag = False

    def __new__(cls,name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    def __init__(self,name):
        if Dog.__inst_fiag == False:
            Dog.__inst_fiag = True
            self.name = name

dog =Dog("旺财")
print(id(dog))
print(dog.name)

dogb = Dog("")
print(id(dogb))
print(dogb.name)