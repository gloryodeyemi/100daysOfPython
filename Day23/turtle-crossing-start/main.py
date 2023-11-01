import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
level = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
game_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()

    # add a new car
    if game_count % 6 == 0:
        cars.add_car()

    # detect when turtle reach the end
    if player.ycor() > 280:
        player.refresh()
        level.increment_level()
        cars.increase_speed()

    # detect turtle collision with car
    for car in cars.cars_list:
        if player.distance(car) < 10:
            game_is_on = False
            level.game_over()

    game_count += 1
    # print(f"Cars length: {len(cars.cars_list)}")

screen.exitonclick()
