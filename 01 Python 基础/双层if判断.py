print("="*15)
username = str(input ("请输入账号："))
passwd = str(input ("请输入密码："))
print("="*15)
if username == "admin" and passwd == "admin":
  print ("登录正常！")
elif username == "admin" and passwd != "admin":
  print ("你输入的密码不正确！")
elif username != "admin" and passwd == "admin":
  print ("你输入的账号不存在！")
