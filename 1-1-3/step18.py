#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    painter.goto(x, y)
    painter.color("gray")
    rem = floor % 6
    if (rem == 0):
        painter.color("red")
    if (rem == 1):
        painter.color("red")
    if (rem == 2):
        painter.color("red")
    rem = floor % 21
    if (rem == 0):

        x = x + 60  # location of next floor
        y = 0

    painter.goto(x,y)
    y = y + 5  # location of next floor

    # draw the floor
    painter.pendown()
    painter.forward(50)



wn = trtl.Screen()
wn.mainloop()