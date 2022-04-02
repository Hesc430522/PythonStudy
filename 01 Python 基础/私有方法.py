class Dog:
    def __send_msg(self):
        print("____正在发送短信_____")

    def send_msg(self,new_money):

        if new_money <= 100:
            print("你的钱多余一百")
        elif new_money <= 100:
            print("你的钱少于一百")

dog = Dog()
#dog.__test1()
dog.send_msg(100)