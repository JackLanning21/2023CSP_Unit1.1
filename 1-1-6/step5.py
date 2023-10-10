#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
spider.pensize(40)
spider.circle(20)
legs = 6
LengthOfLegs = 70
spacing = 380 / legs
spider.pensize(5)
numberoflegs = 0
while (numberoflegs < legs):
  spider.goto(0,0)
  spider.setheading(spacing * numberoflegs)
  spider.forward(LengthOfLegs)
  numberoflegs = numberoflegs + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()