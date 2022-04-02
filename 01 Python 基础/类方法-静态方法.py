class A(object):
    num = 0

    def __init__(self):
        self.name = "王"

    # 类方法,@classmethod 表示静态方法，方法中不用加“self”关键字
    @classmethod
    def add_nem(cls):
        cls.num = 100



