from turtle import *
setup(1024,720,None,None)
pu()
pensize(3)
# bgcolor("")
pencolor("red")
speed(5)
# pd()
seth(60)
for i in range (36):
    goto(0, 100)
    if i!=1:
        pd()
    circle(100, 100)
    goto(0,100)
    circle(-100,100)
    left(10)
speed(2)
goto(0,100)
pensize(8)
pd()
goto(0,-400)
fillcolor("blue")
exitonclick()














