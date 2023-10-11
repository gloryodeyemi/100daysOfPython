from turtle import Turtle, Screen
import random

# initialize the turtle and screen class
cal = Turtle()
cal.shape("turtle")
cal.color("DarkViolet")
cal.speed("normal")
screen = Screen()
screen.colormode(255)


# generate a random color
def random_color():
    return random.randint(0, 255)


# generate a random position
def random_position():
    return random.randint(-100, 100)


# generate a random movement
def random_movement(pace):
    return random.choice([cal.forward(pace), cal.backward(pace)])


# generate a random direction
def random_direction():
    angles = [90, 0, 180, 270]
    return random.choice([cal.left(random.choice(angles)), cal.right(random.choice(angles))])


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
cal.speed("fast")

# challenge 3 - Drawing different shapes
circle_angle = 360
shape_sides = 3

for _ in range(10):
    shape_angle = circle_angle / shape_sides
    for steps in range(shape_sides):
        cal.forward(100)
        cal.right(shape_angle)
    shape_sides += 1
    cal.pencolor((random_color(), random_color(), random_color()))  # change cal color

return_cal()
cal.speed("fastest")

# challenge 4 - Random walk
cal.hideturtle()
for _ in range(300):
    cal.pen(pensize=10, pencolor=(random_color(), random_color(), random_color()))
    random_direction()
    cal.forward(35)

cal.showturtle()
return_cal()

# challenge 5 - Draw a Spirograph
initial_angle = 0

while initial_angle < 360:
    cal.pen(pensize=2, pencolor=(random_color(), random_color(), random_color()))
    cal.circle(100)
    initial_angle += 5
    cal.left(5)

# exit
screen.exitonclick()
