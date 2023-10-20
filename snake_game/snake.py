from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]


class Snake:
    def __init__(self):
        self.square_snakes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(position)
            self.square_snakes.append(new_square)

    def move(self):
        for square_index in range(len(self.square_snakes) - 1, 0, -1):
            new_x = self.square_snakes[square_index - 1].xcor()
            new_y = self.square_snakes[square_index - 1].ycor()
            self.square_snakes[square_index].goto(new_x, new_y)

        self.square_snakes[0].forward(20)
        self.square_snakes[0].left(90)
