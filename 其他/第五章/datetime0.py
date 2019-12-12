# N的阶乘
# def fun(n):
#     if n==1:
#         return 1
#     else:
#         return n*fun(n-1)
# for i in range(10):
#     n=eval(input("请输入一个正整数："))
#     print(fun(n))


from datetime import datetime
today=datetime.now()
print(today)
print(datetime.utcnow())    #世界标准时间（UTC）
someday=datetime(1998,5,13,16,33,32,7)
print(someday)
print(someday.strftime("%Y/%m/%d %H:%M:%S"))
