#   a114_zero_iteration_and_infinite.py
#   Make a zero-iteration condition and follow it with an infinite loop.
#   Include some visual evidence that the second loop is infinite.
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# Add a loop with a zero-iteration condition

start_loop = "y"

while (start_loop == "n"):
    painter.begin_fill()
    painter.forward(40)
    painter.right(90)
    painter.end_fill()

# Add an infinite loop

while (start_loop == "y"):
    painter.begin_fill()
    painter.forward(40)
    painter.right(90)
    painter.end_fill()

wn = trtl.Screen()
wn.mainloop()