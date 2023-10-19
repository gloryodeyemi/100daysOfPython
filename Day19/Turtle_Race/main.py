from turtle import Turtle, Screen
import random

is_race_on = False
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

# print(turtles)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations!!! You win. The {winning_color} turtle is the winner.")
            else:
                print(f"You lose! The {winning_color} turtle is the winner.")

        turtle.forward(random.randint(0, 10))

screen.exitonclick()
