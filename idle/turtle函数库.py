'''
#turtle常用命令汇总，括号中的参数仅仅作为举例使用，可根据需要修改
import turtle
#导入turtle功能模块

turtle.bgcolor("black")
#设置画面背景色

turtle.setup(width=200,height=200,startx=0,starty=0)
#设置窗口大小和在屏幕上的坐标

turtle.bgpic("1.gif")
#设置背景图片，只支持gif格式

turtle.onscreenclick(x，y)
#用户点击屏幕时获得笔的坐标，制作app时响应用户的点击操作32

turtle.bye()
#退出turtle，无任何提示信息

turtle.exitonclick()
#点击后退出turtle

turtle.done()
#关闭turtle，一般在使用完turtle后添加，否则会无响应

turtle.Pen()
#启用画笔

turtle.Pen().color("#cc4455")
#画笔颜色设置，颜色可以使用英文单词或常见的#开头十六进制数表示

turtle.Pen().forward(2)
#画笔前进长度，以像素为单位

turtle.Pen().backward(2)
#画笔后退长度

turtle.Pen().home()
#画笔的初始位置

turtle.Pen().left(90)
#画笔向左转

turtle.Pen().right(90)
#画笔向右转

turtle.Pen().width(3)
#设置画笔宽度，以像素为单位

t=turtle.Pen()
#让t代表turtle.Pen()，上面的内容可以简化
#例如turtle.Pen.color("#cc4455")简化为t.color("#cc4455")
#后面内容都用t表示

t.penup()
#抬起笔，停止写

t.pendown()
#放下笔，开始写

t.write("balabala",font=("Arial",23,"bold"))
#写指定内容”balabala“，并设置字体、字号、加粗等

t.circle(4)
#以参数为半径画圆

t.dot(4)
#以参数为直径画点

t.position()
#笔的坐标（x，y）

t.heading()
#笔的朝向

t.setx(position[0])
#设置笔的x坐标为position记录的x坐标,position由position=t.position()获得

t.sety(position[1])
#设置笔的y坐标为position记录的y坐标

t.setheading(30)
#设置笔的朝向，画笔默认朝向为正右方

t.setpos(x,y)
#设置笔的坐标

t.fillcolor("#33de55")
t.begin_fill()
t.circle(5)
t.end_fill()
#设置填充颜色,开始填充，画圆填充，填充结束

t.goto(x,y)
#笔移动到坐标（x，y）

t.speed(0)
#笔的移动速度参数范围0.5——10，范围之外为0，最快，不设置速度为最慢

t.hideturtle()
#隐藏画笔

t.showturtle()
#显示画笔

t.clear()
#删除画的内容，不修改画笔参数
t.reset()
#删除画的内容，还原画笔参数为初始值
'''
# 五角星
# from turtle import*
# bgcolor("violet")
# setup(800,800,None,None)
# pu()
# pencolor("red")
# pensize(25)
# # fd(-200)
# # write("I Love Python",font=("Arial",60,"bold"))
# fd(-300)
# pd()
# fd(200)
# seth(72)
# fd(200)
# seth(-72)
# fd(200)
# seth(0)
# fd(200)
# seth(216)
# fd(200)
# seth(-72)
# fd(200)
# seth(144)
# fd(200)
# seth(216)
# fd(200)
# seth(72)
# fd(200)
# seth(144)
# fd(200)
# exitonclick()

# from turtle import *
# setup(1024,720,None,None)
# pu()
# pensize(3)
# bgcolor("#eeeeee")
# colormode(255)    可表示rgb颜色
# pencolor(190,190,190)
# pencolor("red")
# goto(200,-200)
# pd()
# goto(-200,-100)
# goto(0,0)
# circle(300,-60)
# circle(-250,-60)
# seth(10)
# pu()
# goto(200,-200)
# speed(20)
# pd()
# circle(100,100)
# circle(-100,100)
# goto(0,0)
# circle(-100,100)
# for i in range (12):
#     goto(0, 0)
#     circle(100, 100)
#     goto(0,0)
#     circle(-100,100)
#     left(30)

# circle(100,100)
# for i in range(12):
#     pu()
#     goto(0, 80)
#     pd()
#     circle(200,-60)
#     left(30)
# for i in range(12):
#     pu()
#     goto(0, 80)
#     pd()
#     circle(-200,-60)
#     left(30)
# pu()
# goto(0,0)
# pensize(8)
# pencolor("violet")
# pd()
# goto(0,-400)
# exitonclick()