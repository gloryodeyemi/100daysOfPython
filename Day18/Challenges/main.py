from turtle import *

# challenge 1 - Draw a Square
square_turtle = Turtle()
square_turtle.shape("turtle")
square_turtle.color("DarkViolet")

for _ in range(4):
    square_turtle.forward(200)
    square_turtle.right(90)

# square_turtle.home()
# clearscreen()

# # algorithmic patterns
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)


screen = Screen()
screen.exitonclick()
