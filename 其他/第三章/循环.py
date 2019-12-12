'''

 list1 = ['Google', 'Runoob', 1997, 2000]   #列表
tup1 = ('Google', 'Runoob', 1997, 2000)    #元组
d = {key1 : value1, key2 : value2 }          #字典
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}   #集合



list = [1, 2, 3, 4]
it  = iter(list)

i = 4
while(i>0):
    print(next(it),end=' ')
    i-=1






import  numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,5,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()
'''

import numpy as np

import matplotlib.pyplot as plt

x=np.linspace(-5,5,1000)  #这个表示在-5到5之间生成1000个x值

y=[1/(1+np.exp(-i)) for i in x]  #对上述生成的1000个数循环用sigmoid公式求对应的y

plt.plot(x,y)  #用上述生成的1000个xy值对生成1000个点

plt.show()  #绘制图像