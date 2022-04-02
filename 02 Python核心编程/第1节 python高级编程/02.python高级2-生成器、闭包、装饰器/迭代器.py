# 1. 可迭代对象
# 以直接作用于 for 循环的数据类型有以下几种：
# 一类是集合数据类型，如 list 、 tuple 、 dict 、 set 、 str 等；
# 一类是 generator ，包括生成器和带 yield 的generator function。
# 这些可以直接作用于 for 循环的对象统称为可迭代对象： Iterable 。

for temp in [10, 12, 13, 25]:  # 迭代器
    print(temp)
a = [1, 2, 3]
aa = (x for x in range(50))  # 迭代器生成器
for temp in aa:
    print(temp)

iter(a)
print(next(a))

# 判断是否可以迭代
from collections import Iterable
# >> a = [11, 22, 33, 44]
# >> isinstance(a, Iterable)
# >> True


# 将元素转换成迭代器
a = [11, 22, 33, 44]
b = iter(a)
next(b)