from turtle import Turtle, Screen
import random

# initialize the turtle and screen class
cal = Turtle()
cal.shape("turtle")
cal.color("DarkViolet")
screen = Screen()
screen.colormode(255)


# generate a random color
def random_color():
    return random.randint(0, 255)


# return cal to original position
def return_cal():
    cal.clear()
    cal.penup()
    cal.home()
    cal.pendown()


# challenge 1 - Draw a square
for _ in range(4):
    cal.forward(100)
    cal.right(90)  # turn to the right by 90 degrees

return_cal()

# challenge 2 - Draw a dashed line
for _ in range(15):
    cal.forward(10)  # move forward
    cal.penup()  # stop drawing line
    cal.forward(10)
    cal.pendown()  # draw line

return_cal()

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

return_cal()

# exit
screen.exitonclick()
