'''
    列表是可以包含0个或者多个对象引用的有序数列
    属于数列类型
    列表的长度没有限制，元素类型可以不同，
    支持成员运算符 （in）
    长度计算函数  （len）
'''
print(list("中国是一个伟大的国家，51zxw.net"))
# 列表的元素类型非常灵活
ls=[425,"BIT",[10,'CS'],425]
# 输出列表
print(ls)
# 输出列表中的列表中的一个字符串元素的最后一个值
print(ls[-2][-1][0])
# print(len(list))
# 计算列表的长度
print(len(ls))

'''
列表必须通过显式的赋值才能得到，
简单的将一个列表赋值给另一个列表不会生成新的列表对象
列如：
'''
lt=ls
ls[0]=0
print(ls)
print(lt)
'''
如上所示，lt仅仅能产生一个新的引用，
即：ls和lt都是实际数据[0, 'BIT', [10, 'CS'], 425]的表示或者引用
因此，修改了ls也同时修改了lt
'''
'''
联系第161页的列表类型的函数
'''
a=[]
b=[]
for i in range(30):
    a.append(i)
    b.append(0)
print(a)
print(b)
# a[::3]=b[2]
# del a[0]
print(a)
del a[0:-1:3]
print(a)
a+=b
print(a)
a.extend(b)
print(a)
del a[20:-1]
del a[-1]
print(a)
a.clear()
b.clear()
print(a)
print(b)
a=list(range(10))
print(a)
print('---------------')
a.reverse()
print(a)
print('---------------')
for i in range (len(a)):
    a[i]=i
    print(a)
print(len(a[3:]))
# 判断元素 X 是否在列表 a 中
print(2 in a)
print(21 in a )
a[3]="python"
print(a)














