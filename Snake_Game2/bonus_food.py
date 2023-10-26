from turtle import Screen
from food import Food
screen = Screen()


class BonusFood(Food):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("red")
        self.hideturtle()

    def show_food(self):
        self.showturtle()

    def hide_food(self):
        self.hideturtle()
