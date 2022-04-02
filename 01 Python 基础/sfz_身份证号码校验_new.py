coefficient = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2] #16位下标
check_code_list = [1,0,'X',9,8,7,6,5,4,3,2]
sum = 0
j   = 0
def main():
    original_sfzh = input("请输入需要校验的身份证号码：")

    if original_sfzh == '':
        print("您没有输入身份证号码,请再次输入:")
        main()
    original_sfzh = original_sfzh.upper()#将x转换成大写
    sfzh_new = original_sfzh[0:17] #从零开始取17位
    #开始判断是否为身份证号码
    for i in sfzh_new:
        global j
        product = coefficient[j] * int(i)
        global sum
        sum = int(product) + sum
        j += 1
    #生成校验码
    check_code = int(sum % 11)
    if original_sfzh != str(sfzh_new) + str(check_code_list[chec43k_code]):
        print("您验证的证件号码为：",original_sfzh)
        print("该身份证号码是错误的,经校验后正确的身份证号码为：",str(sfzh_new) + str(check_code_list[check_code]))
    else:
        print("您验证的证件号码为：", original_sfzh)
        print("该身份证号码无误！")

if __name__ == '__main__':
    main()