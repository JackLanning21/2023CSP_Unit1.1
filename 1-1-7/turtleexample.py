import turtle as trtl

ryan = trtl.Turtle()
jack = trtl.Turtle()
gaunda = trtl.Turtle()
james = trtl.Turtle()
josh = trtl.Turtle()
zach = trtl.Turtle()

turtleList = [ryan, jack, gaunda, james, josh, zach]

x = -100
y = 0

for turtle in turtleList:
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    x = x + 30



wn = trtl.Screen()
wn.mainloop()