from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakelandia")
screen.tracer(0)

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
screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for square_index in range(len(square_snakes) - 1, 0, -1):
        new_x = square_snakes[square_index - 1].xcor()
        new_y = square_snakes[square_index - 1].ycor()
        square_snakes[square_index].goto(new_x, new_y)

    square_snakes[0].forward(20)
    square_snakes[0].left(90)


screen.exitonclick()
