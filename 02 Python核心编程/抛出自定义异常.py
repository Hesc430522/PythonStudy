class ShortInputException():
    def __int__(self,length,atleast):
        self.length = length
        self.atleast = atleast

class b(ShortInputException):

    def main(self):
        try:
            s = input("请输入-->")
            if len(s) <3:
                raise ShortInputException(len(s),3)
        except ShortInputException as result:
            print("你输入的值长度不够至少是%d"%result.atleast)
        else:
            print("没有异常情况")

    main()