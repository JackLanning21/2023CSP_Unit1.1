import turtle as trtl

painter = trtl.Turtle()

painter.pencolor("black")
painter.fillcolor("tan")
painter.begin_fill()
painter.circle(300, 360)
painter.end_fill()

painter.penup()
painter.goto(-100, 250)
painter.pendown()

painter.pencolor("black")
painter.fillcolor("blue")
painter.begin_fill()
painter.circle(50)
painter.end_fill()

painter.penup()
painter.goto(100, 250)
painter.pendown()

painter.pencolor("black")
painter.fillcolor("blue")
painter.begin_fill()
painter.circle(50)
painter.end_fill()

painter.penup()
painter.goto(0, 50)
painter.pendown()

painter.pencolor("black")
painter.fillcolor("red")
painter.begin_fill()
painter.circle(50, 360)
painter.end_fill()

painter.penup()
painter.goto(0, 0)
painter.pendown()




