from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Bet on a turtle", prompt="Which turtle will win the race? (Enter a color): ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []


def turtle_instance(turtle_color):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color)
    return new_turtle


x = -230
y = -100

for color in colors:
    turtle_name = turtle_instance(color)
    turtle_name.penup()
    turtle_name.goto(x=x, y=y)
    turtles.append(turtle_name)
    y += 30

print(turtles)
screen.exitonclick()
