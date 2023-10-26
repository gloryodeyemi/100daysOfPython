from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    """
    Paddle class
    """
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(self.position)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def paddle_up(self):
        """
        Moves the paddle up
        """
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def paddle_down(self):
        """
        Moves the paddle down
        """
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)