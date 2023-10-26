from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from bonus_food import BonusFood

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakelandia")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
bonus_food = BonusFood()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
food_count = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()
        food_count += 1

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for square in snake.square_snakes[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over()

    if food_count % 5 == 0 and food_count != 0:
        bonus_food.show_food()
        # count = 10
        # while count > 0:
        #     count -= 1
        # bonus_food.hide_food()
        # time.sleep(5)

    # detect collision with big food
    if bonus_food.isvisible():
        if snake.head.distance(bonus_food) < 15:
            snake.extend()
            scoreboard.increment_big_score()
            bonus_food.hide_food()

screen.exitonclick()
