from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.refresh_right()

    def refresh_right(self):
        self.goto(x=380, y=280)

    def refresh_left(self):
        self.goto(x=-380, y=280)
