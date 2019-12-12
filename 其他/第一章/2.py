# sum=0
# for i in range(11):#1+2+...+10
#     sum=sum+i
# print(sum)

# str1=input("请输入一个人的名字：")
# str2=input("请输入一个国家的名字：")
# print("世界那么大,{}想去{}看看。".format(str1,str2))


# n=input("请输入一个整数:")
# sum=0
# for i in range(int(n)):
#     sum+=i+1
# print("1到N求和的结果:",sum)

# for i in range (1,10):
#     for j in range (1,i+1):
#         print("{}*{}={:1}".format(j,i,i*j),end='  ')
#     print('')#换行，虽然不知道为什么，但很牛逼

#阶乘1-n-1
# sum,tmp=0,1
# for i in range(1,4):
#     tmp*=i
#     sum+=tmp
# print("运算的结果是:{}".format(sum))

# n=1
# for i in range(5,0,-1):#    -1什么意思?
#     n = (n+1)<<1
# print(n)

#   python 里 “/”表示除（保留小数），“//”表示除（只保留整数），只保留整数部分
# t=3/2
# s=3//2
# print(t)
# print(s)

#2**3=2*2*2     幂运算
# h=3**3
# print(h)
# print(pow(2,2))


# import math                 #import 导入模块
# a=math.floor(22.9)          #模块.函数（取整）
# print(a)
##import 的另外一种使用方法
# from math import sqrt
# t=sqrt(16)
# print(t)
# 引号内的引号可以原样输出，单引号双引号皆可！
# print("let's go to movies!")
# name=input("what's your name?")
# print("hi "+name+"!")
# print('''like this,this is a very long string.It not over here,And it continues."hello world",Still here!''')
# print("hello!!!\nworld!!!")
# 原始字符串 +r    不会把\当作转义字符串，但是不能再原始字符串的结尾输出反斜杠但可以单独把他作为一个字符串来处理
# print(r"c:\nowhere")
# print(r"C:\python\my files\")       wrong!!!
# print(r"C:\python\my files""\\")      right!
# print("%s plus %s equals %s"%(1.5,2.5,4))
# print("Price of eggs: $%d"%46)

# x,y,z=1,2,3
# print(x,y,z,x+y,x>y)

#bool
# print(bool('I think '))     #True
# print(bool(''))             #False
# print(bool('0'))            #True
# print(bool(0))              #False

# a,b=1,1
# if a==b:
#     print('a=b')
# i=1
# sum1=0
# sum2=0
# for i in range(101) :
#     if(i%2==0):
#         sum1+=i
#     else:
#         sum2+=i
# print(sum1,sum2)

#e2.1DrawPython.py
# i=1
# j=1
# while(i<10):
#     j=1
#     while(j<=i):
#         print(i*j)
#         j+=1
#     i+=1
# def tempConvert(ValueStr):
#     if ValueStr[-1] in ['F','f']:
#         C=(eval(ValueStr[0:-1])-32)/18
#         print("转换后的温度是:{:.2f}C".format(C))
#     elif ValueStr[-1] in ['C','c']:
#         F=1.8*eval(ValueStr[0:-1])+32
#         print("转换后的温度是:{:.2f}F".format(F))
#     else:
#         print("输入格式错误！")
# # TempStr=str(input("请输入带有符号的温度值:"))
# TempStr=input("请输入带有符号的温度值:")
# tempConvert(TempStr)
# 上边的代码中，需要注意的是：[0:-1]指的是从零到负一这个区间，含0不含-1
# eval的作用是吧input得到的值进行计算，因为input得到的都是字符类型的
#蛇的制作！
# import turtle
# turtle.setup(800,400,None,None)       #新建一个窗口（窗口长度，窗口宽度，）
# turtle.pu()                      #turtle.setup(width, height, startx, starty)
# turtle.fd(-250)
# turtle.pd()
# turtle.pensize(25)
# # color=["red","black","green","blue","purple","grey"]
# # for i in range (4):
# turtle.pencolor('violet')           #turtle.pencolor((r,g,b))
# turtle.seth(-40)
# for i in range(5):
#     turtle.circle(40,80)
#     turtle.circle(-40,80)
# turtle.circle(40,80/2)
# turtle.fd(40)
# turtle.circle(16,180)
# turtle.fd(40*2/3)
#等腰三角形
# 画笔无方向只有大小，而seth（）决定了它的方向
# from turtle import *
# setup(800,800,None,None)
# pu()
# seth(-120)
# fd(300)
# pd()
# pensize(25)
# pencolor("black")
# seth(0)
# fd(300)
# pencolor("red")
# seth(120)
# fd(300)
# pencolor("violet")
# seth(240)
# fd(300)
#jesus

# from turtle import *
# setup(1920,1080,0,0)
# pensize(25)
# pencolor("violet")
# pu()
# fd(-500)
# seth(90)
# fd(260)
# pd()
# seth(0)
# fd(25)              #   J
# pu()
# seth(-90)
# fd(50)
# pd()
# fd(300)
# circle(-50,180)
# pu()            #   e
# seth(90)
# fd(100)
# seth(0)
# fd(200)
# pd()
# fd(140)
# seth(90)
# circle(70,300)
# pu()            #   s
# fd(200)
# seth(90)
# # fd(10)
# pd()
# seth(90)
# circle(40,280)
# seth(-10)
# circle(-40,280)
# seth(0)
# pu()            #
# fd(150)         #从s到u向上
# seth(90)
# fd(100)
# pd()
# seth(-90)
# fd(100)
# seth(-90)
# circle(40,180)
# seth(90)
# fd(100)
# pu()           #   s
# seth(0)
# fd(150)
# seth(-90)
# fd(30)
# pd()
# seth(90)
# circle(40,280)
# seth(-10)
# circle(-40,280)
# seth(0)
# from turtle import *
# setup(800,800,None,None)
# pu()
# fd(-200)
# seth(-90)
# fd(200)
# pd()
# pencolor('#000000')
# pensize(25)
# seth(60)
# pencolor('#d8baba')
# fd(200)
# seth(-60)
# pencolor('#148647')
# fd(200)
# seth(60)
# pencolor('#0f51a2')
# fd(200)
# seth(180)
# pencolor('#df9145')
# fd(200)
# seth(60)
# pencolor('#21969d')
# fd(200)
# seth(-60)
# pencolor('#4b3a4e')
# fd(200)
# seth(-60)
# pencolor('#00fb23')
# fd(200)
# seth(180)
# pencolor('#0fb827')
# fd(200)
# seth(180)
# pencolor('#4f125a')
# fd(200)


# from turtle import *
# setup(800,800,None,None)
# for i in range (100):
    # speed(10)
    # pensize(3)
    # if(i%4==0):
        # pencolo(r('gold')
    # elif(i%4==1):
    #     pencolor('purple')
    # elif (i % 4 == 2):
    #     pencolor('violet')
    # else:
    #     pencolor('darkgreen')
    # seth(i*90)
    # fd(i*2)


# from turtle import *
# setup(800,800,None,None)
# pu()
# fd(100)
# seth(90)
# fd(100)
# for i in range(4):
#     pu()
#     seth(90+90*i)
#     fd(50)
#     pd()
#     fd(100)
#     pu()
#     fd(50)
# done()

# TempStr=input("请输入一个带有符号的温度值：")
# if TempStr[-1] in['F','f']:
#     C=(eval(TempStr[0:-1])-32)/1.8
#     print("转换后的温度是：{:.0f} C".format(C))
# elif TempStr[-1] in ['c','C']:
#     F=eval(TempStr[0:-1])*1.8+32
#     print("转换后的温度是：{:.0f} F".format(F))
# else:
#     print("输入格式错误！")

# int(T=input("请输入温度值："))
# T=0
from turtle import*
setup(800,800,None,None)
goto(-300,-300)

goto(-300,300)
done()

















