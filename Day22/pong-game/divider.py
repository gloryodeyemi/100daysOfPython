from turtle import Turtle

STARTING_POSITIONS = [(0, 280), (0, 220), (0, 160), (0, 100), (0, 40), (0, -20), (0, -80), (0, -140), (0, -200), (0, -260)]


class Divider:
    def __init__(self):
        self.dividers = []
        self.create_divider()

    def create_divider(self):
        for position in STARTING_POSITIONS:
            new_divider = Turtle(shape="square")
            new_divider.shapesize(stretch_wid=2, stretch_len=0.5)
            new_divider.color("white")
            new_divider.penup()
            new_divider.goto(position)
            self.dividers.append(new_divider)
