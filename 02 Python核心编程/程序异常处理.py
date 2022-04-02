#codlig=utf-8
try:
    #pri nt(num)
    11/0
    open("xxx.txt")
    print("-" * 10 + "1" + "-" * 10)

except (NameError,FileNotFoundError):
    print("-"*10+"抛出异常"+"-"*10)

except Exception as ret:
    print(ret)
    print("如果用了Exception上面的Exception")
else:
    print("没有异常")

finally:
    print("_____finally------")

print("-"*10+"2"+"-"*10)