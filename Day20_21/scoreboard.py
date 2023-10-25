from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write_score()
        # self.clear()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=('Phenomena', 15, 'bold'))

    def increment_score(self):
        self.score += 1
        self.write_score()
