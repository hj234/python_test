# 数组定义
student=['Jack','Bob','Harry','Micle']
# 不能带引号输出数组
print('student')
print(student)
# 访问数组元素
print(student[0])   #第一个元素
print(student[3])
print(student[-1]) #最后一个元素
# 数组越界
# IndexError: list index out of range
# print(student[4]) #一共只有四个元素：0 1 2 3 -------4不在数组范围之内 访问不到
# 在数组（列表）最后一个元素后边添加一个元素
student.append('51zxw.net')
print(student)
# 在数组的第 i 位置插入一个元素
student.insert(0,'51zxw.net')
student.insert(0,'hello')
print(student)
# 数组替换
student[0]='No.1'
print(student)

# 删除元素
# 删除末尾元素
student.pop()
print(student)
# 删除特定位置元素
student.pop(1)
print(student)

student.append('Nike')
student.append('Rose')
student.append(21)
student.append(9527)
student.insert(2,18)
print(student)

