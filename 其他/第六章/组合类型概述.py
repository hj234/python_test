# ls=[1,2,5,0]
# print(all(ls))
# print(hash('hello world'))
# print(id(ls))
# print(list(reversed(ls)))
# print(sorted(ls,reverse=True))
# print(type(ls))
# # print(type(reverse(ls)))
#
#
# print(hex(1024))
# print(hex(12800))
# print(hex(65536))

# 列表
'''
# L=[9,1,8,6,5,4,2]
# L.sort()
# print(L)
# '''
#
# # 字符串
# '''
# a='xydz'
# print(a[::-1])
# '''
#
# # 字典    字典前面为键后面的叫值
# a={1:1,2:2,3:3}
# b=[]
# for key in a.keys():
#     b.append(key)
# b.sort()
# print(",".join(str(x) for x in b))
# '''
# PS:这里说一下join的用法,“，”.join(b) 意思就是将b字符串用‘，’拼接起来并组成一个字符串/
# str(i)把i这个整数转化为字符串
# '''

# creature="cat","dog","tigter","human"
# print(creature)

# ls=[2,5,7,1,6]
# print(ls)
# # 列表排序
# # 升序
# a=sorted(ls)
# print(a)
# # 降序
# a.sort(reverse=1)
# print(a)
# #比较列表
# ls1=[30,1,2,0]
# ls2=[1,21,133]
# if ls1>ls2:
#     print(True)
# else:
#     print(False)
#

# from math import *
# def getNum():       #输入数据
#     nums=[]
#     iNumStr=input("请输入一个数字(直接输入回车键退出):")
#     while iNumStr != "":
#         nums.append(eval(iNumStr))
#         iNumStr = input("请输入一个数字(直接输入回车键退出):")
#     return nums
# def mulit(n):
#     s=1
#     for i in n:
#         s*=i
#     return s
# n=getNum()
# print(mulit(n))
def h(n):
    print("+",end="")
    for i in range(n):
        print(" - - - - +",end="")
    return "\r"
def l(n):
    for i in range(n):
        print("|         ",end="")
    print("|")
    return "\r"
n=eval(input("please input a integer:"))
for i in range(n*3+1):
    if i%3==0:
        print(h(n))
    else:
        print(l(n))







