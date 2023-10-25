import time
from food import Food


class BigFood(Food):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("red")
        self.hideturtle()

    def show_food(self):
        self.refresh()
        self.showturtle()
        # time.sleep(10)
        self.hide_food()

    def hide_food(self):
        self.hideturtle()
