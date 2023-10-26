from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create the paddles
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# create the ball
ball = Ball()

# create the scores
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.paddle_up, "Up")
screen.onkey(r_paddle.paddle_down, "Down")
screen.onkey(l_paddle.paddle_up, "w")
screen.onkey(l_paddle.paddle_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when ball misses the right paddle
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_point()

    # detect when ball misses the left paddle
    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_point()

screen.exitonclick()
