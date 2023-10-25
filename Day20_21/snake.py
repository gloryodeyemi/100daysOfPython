from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.square_snakes = []
        self.create_snake()
        self.head = self.square_snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.square_snakes.append(new_square)

    def extend(self):
        self.add_square(self.square_snakes[-1].position())

    def move(self):
        for square_index in range(len(self.square_snakes) - 1, 0, -1):
            new_x = self.square_snakes[square_index - 1].xcor()
            new_y = self.square_snakes[square_index - 1].ycor()
            self.square_snakes[square_index].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
