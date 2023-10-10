from turtle import Turtle, Screen
import random

cal = Turtle()
cal.shape("turtle")
cal.color("DarkViolet")
screen = Screen()
screen.colormode(255)


def random_color():
    return random.randint(0, 255)


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

cal.clear()
cal.penup()
cal.home()
cal.pendown()

# challenge 3 - Drawing different shapes
circle_angle = 360
shape_sides = 3

for _ in range(10):
    angle = circle_angle / shape_sides
    for steps in range(shape_sides):
        cal.forward(100)
        cal.right(angle)
    shape_sides += 1
    cal.pencolor((random_color(), random_color(), random_color()))  # change cal color


# # algorithmic patterns
# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)


screen.exitonclick()
