'''
import sys
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))
'''
'''
a=10
b=3
print('%.1lf'%(a/b))
print("%.1lf"%(a/b)
'''
'''
# 求三位数的第一种方法
c=0
for i in range (1,5):
    for j in range(1,5):
        for k in range (1,5):
            if (i!=k)and(k!=j)and(i!=j):
                print(i,j,k)
                c+=1
print(c)
'''
'''
# 第二种
for i in range (1,10):
    for j in range (1,i+1):
        print("{}*{}={} ".format(j,i,i*j),end="")
    print("\n")
'''
'''
# 第三种
d=[]
for i in range (1,5):
    for j in range (1,5):
        for k in range (1,5):
           if (i!=k) and (k!=j) and (i!=j):
            d.append(i*100+j*10+k)
print(d)
print(len(d))
'''
'''
# 第四种
list_num = [1,2,3,4]
list  = [i*100 + j*10 + k for i in list_num for j in list_num for k in list_num if (j != i and k != j and k != i)]
print (list)
'''
'''
# 第五种
将 for if 整合到一句里面
ls=[1,2,3,4]
ls=[i*100+j*10+k for i in ls for j in ls for k in ls if(i!=j and i!=k and j!=k)]
print(ls)
'''
'''
# 第六种
# 利用集合进行判断
# 利用集合排除重复元素

ls=['1','2','3','4']
sum=[]
for i in ls:
    for j in ls :
        for k in ls :
            if (len(set(i+j+k)))==3:
                # sum.append(eval(i+j+k))
                # sum.append(int(i+j+k))
                sum+=[eval(i+j+k)]
                # sum+=[int(i+j+k)]
#       上边的四条语句性质一样
#       都是将sum这个列表元素加1
print(sum)
print(len(sum))
'''
'''
# 第七种
# 移位运算
# 不很理解
for num in range(6,58):
    a = num >> 4 & 3
    b = num >> 2 & 3
    c = num & 3
    if( (a^b) and (b^c) and (c^a) ):
        print(a+1,b+1,c+1) 
'''

ls=['1','2','3','4']
sum=[]
for i in ls:
    for j in ls :
        for k in ls :
            if (len(set(i+j+k)))==3:
                # sum.append(eval(i+j+k))
                # sum.append(int(i+j+k))
                sum+=[eval(i+j+k)]
                # sum+=[int(i+j+k)]
#       上边的四条语句性质一样
#       都是将sum这个列表元素加1
print(sum)
print(len(sum))


