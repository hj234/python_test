# 4.1猜数游戏：
# import random
# # random.seed(0)
# t=random.randint(0,10)
# n=eval(input("please input n(0,9):"))
# sum=0
# while(1):
#     if n>t:
#         print("遗憾，太大了")
#         sum+=1
#     if n<t:
#         print("遗憾，太小了")
#         sum+=1
#     if n==t:
#         sum+=1
#         print("预测{}次，预测成功！".format(sum))
#         break
#     n = eval(input("please input n:"))

# 4.2统计不同字符的个数
# s=input("plesae input a string:")
# w,n,p,t=0,0,0,0
# for i in s:
#     if(ord('a')<=ord(i)<=ord('z') or ord('A')<=ord(i)<=ord('Z')):
#         w+=1
#     elif(ord(i)==ord(' ')):
#         p+=1
#     elif(ord('0')<=ord(i)<=ord('9')):
#         n+=1
#     else:
#         t+=1
# print("words:{}\nnumbers:{}\nspace:{}\nothers:{}".format(w,n,p,t))


#4.3最大公约数的计算
# a=eval(input("plesae input a:"))
# b=eval(input("plesae input b:"))
# m,n=a,b
# while b:
#    a,b=b,a%b
# print("最大公约数:{}\n最小公倍数:{:.0f}".format(a,m*n/a))

# 4.4猜数字游戏续
# import random
# t=random.randint(0,100)
# n=eval(input('plesae input a number from 0 to 100:'))
# sum=0
# while(1):
#     if n>t:
#         print("遗憾，太大了")
#         sum+=1
#     if n<t:
#         print("遗憾，太小了")
#         sum+=1
#     if n==t:
#         sum+=1
#         print("预测{}次，预测成功！".format(sum))
#         break
#     n = eval(input("please input n:"))




