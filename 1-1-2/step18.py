# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# set the pen and fill colors
# then draw a circle
painter.pencolor("blue")
painter.fillcolor("red")
painter.begin_fill()
painter.circle(100)
painter.end_fill()

# move the turtle to another part of the screen
painter.penup()
painter.goto(-120, -250)
painter.pendown()

# change both the pen and fill colors
# then draw a polygon of your choice

painter.pencolor("yellow")
painter.fillcolor("blue")
painter.begin_fill()
painter.circle(120, 360, 6)
painter.end_fill()

painter.penup()
painter.goto(120, -250)
painter.pendown()

painter.pencolor("green")
painter.fillcolor("brown")
painter.begin_fill()
painter.circle(150, 360, 9)
painter.end_fill()

painter.penup()
painter.goto(120, 250)
painter.pendown()

painter.pencolor("black")
painter.fillcolor("red")
painter.begin_fill()
painter.circle(75, 360, 7)
painter.end_fill()

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()