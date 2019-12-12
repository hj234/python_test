
# 未知输入数据组数
# while True:
#     try:
#         a,b=map(int,input().strip().split())
#         print(a+b)
#     except EOFError:
#         break

# 有限组输入
# case=eval(input())
# for i in range(case):
#     a,b=map(int,input().split())
#     print(a+b)


# while 1:
#     try:
#         a,b=map(int,input().split())
#         print(a+b)
#     except EOFError:
#         break


# n=int(input())
# for i in range(n):
#     a,b=map(int,input().split())
#     print(a+b)

def p(n):
    if(n==0):
        return 1
    else:
        return n*p(n-1)
while 1:
    try:
        n=int(input())
        print(p(n))
    except EOFError:
        break




