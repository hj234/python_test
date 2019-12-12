from math import *
def getNum():       #输入数据
    nums=[]
    iNumStr=input("请输入一个数字(直接输入回车键退出):")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入一个数字(直接输入回车键退出):")
    return nums
def mean(numbers):  #计算平均值
    s=0.0
    for num in numbers:
        s=s+num
    return s/len(numbers)
def dev(numbers,mean):
    sdev=0.0
    for num in numbers:
        sdev=sdev+(num-mean)**2
    return sqrt(sdev/(len(numbers)-1))
def median(numbers):
    numbers.sort()
    size=len(numbers)
    if size%2==0:
        med=(numbers[size//2-1]+numbers[size//2+1])/2
    else:
        med=numbers[size//2]
    return med
n=getNum()
m=mean(n)
print("平均值：{},方差：{:.2}，中位数{}.".format(m,dev(n,m),median(n)))



