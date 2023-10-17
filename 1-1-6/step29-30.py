#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
# Create the body of the spider
spider.pensize(40)
spider.circle(20)
# Configure the spider legs
legs = 8
LengthOfLegs = 70
spacing = 360 / legs
spider.pensize(5)
numberoflegs = 0
# Draw the legs
while (numberoflegs < legs):
    if (numberoflegs < 4):
        spider.goto(0,20)
        spider.setheading(spacing * numberoflegs * .5)
        spider.forward(LengthOfLegs)
        numberoflegs = numberoflegs + 1
    else:
        spider.goto(0, 20)
        spider.setheading(spacing * numberoflegs * -.5)
        spider.forward(LengthOfLegs)
        numberoflegs = numberoflegs + 1
# Create the eyes
spider.pensize(10)
spider.circle(5)
spider.goto(0,  10)



spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()