# import turtle
# import time
#
# turtle.pensize(5)
# turtle.pencolor("yellow")
# turtle.fillcolor("red")
#
# turtle.begin_fill()
# for _ in range(5):
#     turtle.forward(200)
#     turtle.right(144)
# turtle.end_fill()
# time.sleep(2)
#
# turtle.penup()
# turtle.goto(-150, -120)
# turtle.color("violet")
# turtle.write("Done", font=('Arial', 40, 'normal'))
#
# turtle.mainloop()

import turtle
import time
turtle.setup(1280,720)
turtle.pensize(5)
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(5):
    turtle.fd(300)
    turtle.right(144)
turtle.end_fill()
turtle.hideturtle()
time.sleep(1)
turtle.pu()
turtle.goto(-300,-200)
turtle.write("我爱中国",font=("Arial",50,"bold"))
turtle.exitonclick()






