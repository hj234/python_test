'''
一个整数加上100和268后都是一个完全平方数，请问该数是多少
'''
# 基本上不需要费脑子
import math
for i in range(10001):
    m=int (math.sqrt(i+100))
    n=int (math.sqrt(i+268))
    if(m*m==(i+100) and n*n==(i+268)):
        print(i)
        break