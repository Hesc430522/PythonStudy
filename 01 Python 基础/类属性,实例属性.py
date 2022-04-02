import random


class Tools(object):
    num = random.randint(1, 100)

    # 定义一个私有方法
    def __init__(self):
        Tools.num += 1

    def test(self, num):
        if num >= 100 and num != 0:
            print("你的钱多余或等于一百")
        elif num <= 100 and num != 0:
            print("你的钱少余或等于一百")
        elif num == 0:
            print("你没有钱")


tools = Tools()
tools.test(Tools.num)
print(Tools.num)
