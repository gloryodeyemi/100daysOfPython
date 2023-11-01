from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment_level(self):
        self.level += 1
        self.write_score()
