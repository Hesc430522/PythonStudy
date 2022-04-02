coefficient = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2] #16位下标
j = 0
sum = 0

sfzh = input("请输入一个身份证号码：")
sfzh = '34052419800101001X'
sfzh_ = sfzh[0:17] #17位下标

for i in sfzh_:
    min = coefficient[j] * int(i)
    sum = min + sum
    print(sum)
    min = (sum % 11)
    j += 1
    print(min)

'''
if min == 0:
   sfzh_new = sfzh_ +'1'
   if sfzh_new == sfzh:
       print('恭喜你,你输入的证件号是正确的！')
       print(sfzh_new)
   else:
       print('是错误的身份证号！')
       print(sfzh,">>>您输入的身份证号")
       print(sfzh_new,">>>验证后的身份证号")

#-------------1----------------
elif min == 1:
    sfzh_new = sfzh_ + '0'
    if sfzh_new == sfzh:
        print('恭喜你,你输入的证件号是正确的！')
        print(sfzh_new)
    else:
        print('是错误的身份证号！')
        print(sfzh, ">>>您输入的身份证号")
        print(sfzh_new, ">>>验证后的身份证号")

elif min == 2:
    sfzh_new = sfzh_ + 'X'
    if sfzh_new == sfzh:
        print('恭喜你,你输入的证件号是正确的！')
        print(sfzh_new)
    else:
        print('是错误的身份证号！')
        print(sfzh, ">>>您输入的身份证号")
        print(sfzh_new, ">>>验证后的身份证号")

elif min == 3:
    sfzh_new = sfzh_ + '9'
    if sfzh_new == sfzh:
        print('恭喜你,你输入的证件号是正确的！')
        print(sfzh_new)
    else:
        print('是错误的身份证号！')
        print(sfzh, ">>>您输入的身份证号")
        print(sfzh_new, ">>>验证后的身份证号")
elif min == 4:
    sfzh_new = sfzh_ + '8'
    if sfzh_new == sfzh:
        print('恭喜你,你输入的证件号是正确的！')
        print(sfzh_new)
    else:
        print('是错误的身份证号！')
        print(sfzh, ">>>您输入的身份证号")
        print(sfzh_new, ">>>验证后的身份证号")

elif min == 5:
    sfzh_new = sfzh_ + '7'
    if sfzh_new == sfzh:
        print('恭喜你,你输入的证件号是正确的！')
        print(sfzh_new)
    else:
        print('是错误的身份证号！')
        print(sfzh, ">>>您输入的身份证号")
        print(sfzh_new, ">>>验证后的身份证号")

elif min == 6:
    sfzh_new = sfzh_ + '6'
    if sfzh_new == sfzh:
        print('恭喜你,你输入的证件号是正确的！')
        print(sfzh_new)
    else:
        print('是错误的身份证号！')
        print(sfzh, ">>>您输入的身份证号")
        print(sfzh_new, ">>>验证后的身份证号")



elif min == 7:
    sfzh_new = sfzh_ + '5'
    if sfzh_new == sfzh:
        print('恭喜你,你输入的证件号是正确的！')
        print(sfzh_new)
    else:
        print('是错误的身份证号！')
        print(sfzh, ">>>您输入的身份证号")
        print(sfzh_new, ">>>验证后的身份证号")

elif min == 8:
    sfzh_new = sfzh_ + '4'
    if sfzh_new == sfzh:
        print('恭喜你,你输入的证件号是正确的！')
        print(sfzh_new)
    else:
        print('是错误的身份证号！')
        print(sfzh, ">>>您输入的身份证号")
        print(sfzh_new, ">>>验证后的身份证号")

elif min == 9:
    sfzh_new = sfzh_ + '3'
    if sfzh_new == sfzh:
        print('恭喜你,你输入的证件号是正确的！')
        print(sfzh_new)
    else:
        print('是错误的身份证号！')
        print(sfzh, ">>>您输入的身份证号")
        print(sfzh_new, ">>>验证后的身份证号")

elif min == 10:
    sfzh_new = sfzh_ + '2'
    if sfzh_new == sfzh:
        print('恭喜你,你输入的证件号是正确的！')
        print(sfzh_new)
    else:
        print('是错误的身份证号！')
        print(sfzh, ">>>您输入的身份证号")
        print(sfzh_new, ">>>验证后的身份证号")
        '''
