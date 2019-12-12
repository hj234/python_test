T=input("请输入温度值：")
x=input("请输入温度符号")
if x in ['F','f']:
    C=(int(T)-32)/1.8
    print("转换后的温度是：{:.0f} C".format(C))
elif x in ['c','C']:
    F=int(T)*1.8+32
    print("转换后的温度是：{:.0f} F".format(F))
else:
    print("输入格式错误！")