# plaincode = input("请输入明文：")
# for p in plaincode:
#     if ord("a")<=ord(p)<=ord("z"):
#         print(chr(ord("a")+(ord(p)-ord("a")+3)%26),end='')
#     else:
#         print(p,end='')


# print("python".center(40,' '))
# print("python is an excellent language.".split())
# t=ord('a')
# n=ord('A')
# print(t)
# print(n)
#
# print(chr(97),chr(65),end='')
# print("{0:.3},  {0:.4},  {0:.5}".format(3.1415926))
# print("{0:.3f}, {1:.3f},  {2:.3f},  {3:.3f}".format(123.1234,234.567,345.678,678.789))
# print("{0:e}, {1:.3e},  {2:.4e},  {3:.5e}".format(123.1234,234.567,345.678,678.789))


# import decimal
# a=decimal.Decimal('3.141592653')
# b=decimal.Decimal('1.234567898')
# print(a*b)

# from decimal import*
# a=Decimal('3.1415926')
# b=Decimal('1.234567898')
# print(a*b)

# print(pow(2,100))
# print(pow(2,500))
# a='3273390607896141870013189696827599152216642046043064789483291368096133796404674554883270092325904157150886684127560071009217256545885393053328527589376'
# print(len(a))

# import sys
# print(sys.float_info)
# print(1111122222.3333355555)
# print((1.23+4j).imag  , 1.23+4j.real)
# print((123.456+321.654j).real)
# print((123.456+321.654j).imag)

# i=0
# while i<=10:
#     a=int(input("请输入一个整数:"))
#     print(abs(a))
#     i+=1

# print(complex(10,20))

# print(30-3**2+8//3**2*10)

# import math
# print(math.ceil(15.2))
# print(math.floor(15.2))
# print(math.pi)
# print(math.e)
# print(math.factorial(6))
# print(math.gcd(10,15))
# print(math.fsum([1,2,3,4,5,6,7,8,9]))
# print(math.degrees(5))
# print(math.radians(360))
# print(math.acos(-1.0))

# import math
# dayup=math.pow(1.0+0.001,365)
# daydown=math.pow(1.0-0.001,365)
# print("dayup:{0: ^20.5f}\ndaydown:{1: ^20.5f}".format(dayup,daydown))
# print("测试：{0: <30,d}".format(123456789))
# 参数序号，引用符号：，对齐<>^，宽度，数字千位分隔符，精度（.2），类型（）

# name="Python 语言程序设计"
# print(name[0:6])
# print(name[0:-1])
# print(name[0])
# print("python\t程序\t语言\t设计")

# week="星期一星期二星期三星期四星期五星期六星期日"
# t=int(input("请输入星期数字(1-7):"))
# print(week[3*(t-1):3*t])

# s="Python Sring"
# print(s.upper())
# print(s.lower())
# print(s.find('i'))
# print(s.islower())
# print(s.isupper())
# print(s.isprintable())
# print(s.isnumeric())
# print(s.isspace())
# print(s.endswith("S",0,8))
# print(s.startswith('P'))
# print('stand'.endswith('n',0,4))
# print('123124125'.split(sep=None,maxsplit=-1))    #字符串的分割，以sep的界
# print('123124125126127128129'.count('3',0,3))     #统计字符串出现的次数（“字符串”，开始位置，结束位置（不含））
# print('1and2and3and4and5and6and7and8and9and10'.replace('and','hate',5))       #字符串的替换
# print('666'.center(20,' '))                         #字符居中
# print('love beautiful gril'.strip('l'))
# print('The mid autume festival'.zfill(10))
# print("{}".format(hex(100)))
# print(oct(100))
# print(bin(100))
# print(ord('s'))
# print(chr(10004))
# print(chr(9801))
# print(len('1214451151616561561321531'))
# print('{0:b}\n{0:c}\n{0:d}\n{0:o}\n{0:x}\n{0:X}'.format(9801))
# print("{0:.3e}\n{0:.3E}\n{0:.3f}\n{0:.3%}".format(9801))
# print("{:>15s}:{:<8.2f}".format("length",23.87501))
# print("{0:b}\n{0:o}\n{0:d}\n{0:x}\n{0:c}".format(389))

# import time
# scale = 10
# print("-------执行开始------")
# for i in range(scale+1):
#     a,b='**'*i,'..'*(scale-i)
#     c=(i/scale)*100
#     print("{:^3.0f}%[{}->]{}]".format(c,a,b))
#     time.sleep(0.1)
# print('------执行结束------')


# s='hello'
# print(s)
# print(s[0::4])
# print(s[-2::-1])
# print(s[::-2])
# str1 = 'i2el54ovvvb4e3byero32u56f;$o43vsfe67r0c 99'
# print(str1[::3])
# dayup, N = 1.0, 0.001
# while (N <= 0.01):
#     for i in range(365):
#         if i % 7 in [0, 5, 6]:
#             dayup = dayup * 1.0
#         else:
#             dayup = dayup * (1.0 + N)
#     print("N=:{:.3f}\t年终值是：{:.2f}.".format(N, dayup))
#     N = N + 0.001

dayup, N = 1.0, 0
while N <= 0.010:
    N = N + 0.001
    for i in range(365):
        if i % 7 in [0, 5, 6]:
            dayup = dayup * 1.0
        else:
            dayup = dayup * (1.0 + N)
    print("N=:{:.3f}\t年终值是：{:.2f}".format(N, dayup))

