#数组输出
student=['Jack','Mary','Bob','Harry','Micle']
print(student)
#数组输出（特定值）
print(student[0])
print(student)
#数组添加（添加到最后一个元素）
student.append('51zxw')
print(student)
#数组添加（添加到特定位置）
student.insert(0,'hello')
print(student)
#替换特定数组
student[0]='No.1'
print(student)
#删除末尾数组
student.pop()
print(student)
#删除特定位置数组
student.pop(-1)
print(student)
#元组
course=('Chinese','Math','Computer','English')
print(course)
print(course[0])
print(course[-1])
print(course[0:3])
#索引位置为1之后所有元素(含1)
print(course[1:])
#索引位置为1之前的所有元素（不含1）
print(course[:1])
#输出元组的元素个数
print(len(course))


#条件判断
score=80
if score>=80:
    print("A")
else:
    print("B")


score=75

if score>80:
    print("score is A")
elif score>=60:
    print("score is B")
else:
    print("score is C")



#循环语句  for循环：
student=["jack","Bob","Marry","Miacl"]
for stu in student:
    print(stu)

sum=0
for i in range(11):
    sum=sum+i
print(sum)

#while循环：只要条件满足，就不断循环，条件不符满足退出循环
n=10
while n>0:
    n=n-1
    print(n)
print("over!")

