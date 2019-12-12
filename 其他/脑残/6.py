import math
import sys
a,b,c,d=map(int,input().split())
# print(a,b,c,d)
ans=math.factorial(a+b+c+d)
sum1=math.factorial(a)
sum2=math.factorial(b)
sum3=math.factorial(c)
sum4=math.factorial(d)
ans=ans//sum1//sum2//sum3//sum4
print(ans%1000000007)


# sum=[1,1,1,1]
# # sum1=1
# # sum2=1
# # sum3=1
# # sum4=1
# ans=1
# num=0
# a=1
# for line in sys.stdin:
#     a=int(line)
#     print(a)
# #     num+=a
# #     sum[i]=math.factorial(a)
# #     i+=1
# # ans=math.factorial(num)
# # for i in range(4):
# #     ans=ans//sum[i]
# # print(ans%1000000007)
