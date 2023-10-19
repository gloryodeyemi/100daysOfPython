from turtle import Turtle, Screen

sketchy = Turtle()
sketchy.shape("turtle")
sketchy.color("blue")
screen = Screen()


def forward_move():
    sketchy.forward(20)


def backward_move():
    sketchy.backward(20)


def clockwise():
    sketchy.right(45)


def counter_clockwise():
    sketchy.left(45)


def clear():
    sketchy.clear()
    sketchy.penup()
    sketchy.home()
    sketchy.pendown()


def sketch():
    screen.listen()
    screen.onkey(key="W", fun=forward_move)
    screen.onkey(key="S", fun=backward_move)
    screen.onkey(key="A", fun=counter_clockwise)
    screen.onkey(key="D", fun=clockwise)
    screen.onkey(key="C", fun=clear)


sketch()

screen.exitonclick()
