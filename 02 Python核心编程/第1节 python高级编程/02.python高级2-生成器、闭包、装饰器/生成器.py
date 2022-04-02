# 生成器语句
print("1、生成器创建方法")
# 第一种
i=1
a = (x for x in range(11))  # 不会全部显示
while i <= 11:  # 循环使用Next打印a的内容
    print(next(a))  # 显示生成器数据
    i+=1

# 第二种
b = [xx for xx in range(101)]  # 使用列表保存数据列表
print(b)    # 直接显示


print("="*50+"分隔符"+"="*50)


# 创建生成器函数
def creatnum():
    print("start")
    aa, b = 0, 1
    for i in range(10):
        yield b
        aa, b = b, aa + b
    print("stop")


aa = creatnum()
# 生成器调用方法
# 1、使用for调用
for test_aa in aa:
    print(test_aa)

# 2、使用__next__调用
# ret = aa.__next__()
# print(ret)

# 3、使用next()调用
# print(next(aa))

print("="*50+"分隔符"+"="*50)
print("2、生成器sed利用")
def test():
    i = 0
    while i<= 5:
        temp = yield i
        print(temp)

        i+=1

t = test()

print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.__next__())
