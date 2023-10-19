from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
# Higher order function - function that can work with another function
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
