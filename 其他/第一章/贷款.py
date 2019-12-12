#calLoan.py
a=float(input("请输入贷款总量："))
b=int(input("请输入还款年限："))
cg=input("还款方式：（C or G）")
if cg in ['C','c']:
    if (0 < b <= 1):
        p = 6.00/100
    elif 1<b <= 3:
        p = 6.15/100
    elif 3<b <= 5:
        p = 6.40/100
    else:
        p = 6.55/100
    m = a * 10000 * (p / 12) * (1 + p / 12) ** (12 * b) / ((1 + p / 12) ** (12 * b) - 1)
    print(m)
elif cg in ['G','g']:
    if (0 < b <=5):
        p = 4.00/100
    else:
        p = 4.50/100
    m = a * 10000 * (p / 12) * (1 + p / 12) ** (12 * b) / ((1 + p / 12) ** (12 * b) - 1)
    print(m)
else :
    print('输出格式错误！')
