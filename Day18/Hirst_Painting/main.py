import colorgram
import random
from turtle import Turtle, Screen


# extract colors from the image
def extract_colors(image):
    painting_colors = colorgram.extract(image, 50)
    colors = []
    for _ in range(len(painting_colors)):
        color_tuple = ()
        color = painting_colors[_].rgb
        color_tuple += (color.r, color.g, color.b)
        colors.append(color_tuple)

    return colors


# print(extract_colors('image.jpeg'))
color_list = [(174, 166, 150), (126, 99, 75), (232, 225, 229), (61, 101, 131), (132, 163, 182), (127, 76, 92),
              (18, 37, 60), (179, 142, 156), (61, 119, 94), (153, 139, 80), (196, 195, 178), (144, 172, 160),
              (64, 27, 40), (116, 36, 54), (172, 102, 121), (62, 39, 28), (74, 157, 137), (12, 99, 76), (185, 103, 85),
              (122, 39, 33), (15, 49, 39), (34, 59, 106), (73, 153, 165), (110, 122, 160), (79, 82, 28), (10, 88, 103),
              (211, 180, 190), (172, 203, 193), (216, 180, 175), (166, 203, 210), (183, 188, 205)]


# generate a random color
def random_color(colors):
    return random.choice(colors)


# initialize the turtle class
cal = Turtle()
cal.shape("turtle")
cal.color("DarkViolet")
cal.speed("fast")

# initialize the screen class
screen = Screen()
screen.colormode(255)
height = screen.window_height()
width = screen.window_width()
screen.setworldcoordinates(-100, -100, screen.window_width() - 100, screen.window_height() - 100)

initial_height = height - 50
for i in range(10):
    cal.showturtle()
    for j in range(10):
        cal.pendown()
        cal.dot(20, random_color(color_list))
        cal.penup()  # stop drawing line
        cal.forward(50)
    cal.hideturtle()
    cal.setpos(-1, height - initial_height)
    initial_height -= 50
cal.hideturtle()

# exit
screen.exitonclick()
