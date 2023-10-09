from turtle import Turtle, Screen

cal = Turtle()
cal.shape("turtle")
cal.color("DarkViolet")
screen = Screen()

# challenge 1 - Draw a square
for _ in range(4):
    cal.forward(100)
    cal.right(90)

cal.clear()

# challenge 2 - Draw a dashed line
for _ in range(15):
    cal.forward(10)
    cal.penup()
    cal.forward(10)
    cal.pendown()

# # algorithmic patterns
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)


screen.exitonclick()
