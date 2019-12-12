'''
输入三个整数x,y,z，请把这三个数由小到大输出
'''
# x,y,z=input(),input(),input()
# int(x,y,z)
x=input()
y=input()
z=input()
int(eval(x))
int(eval(y))
int(eval(z))
if(x>y>z):
    print(x,y,z)
elif(x>z>y):
    print(x,y,z)
elif(y>z>x):
    print(y,z,x)
elif(y>x>z):
    print(y,x,z)
elif(z>x>y):
    print(z,x,y)
else:
    print(z,y,x,)



