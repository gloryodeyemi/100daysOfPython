from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakelandia")

square_snakes = []


def snake_instance():
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    return new_turtle


x = 0
y = 0

for index in range(3):
    new_snake = snake_instance()
    new_snake.penup()
    new_snake.goto(x=x, y=y)
    square_snakes.append(new_snake)
    x -= 20


screen.exitonclick()
