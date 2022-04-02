import  time

old_file =open("users.csv",'rt',encoding='utf-8')
new_file = open("用qq邮箱注册的账号.txt","a")

while True:
    lines = old_file.readline().split('\n')
    time.sleep(0.05)
    for line in lines:

        if len(line) ==0:
            break

        elif '@qq.com' in line:
            #print(line)
            new_file.write("\r"+line)

        elif '@QQ.COM' in line:
            #print(line)
            new_file.write("\r"+line)
        else:
            break

new_file.close()
old_file.close()