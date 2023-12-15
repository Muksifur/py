import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("THE PONG GAME")
screen.tracer(2)
ball = Ball()
scoreboard = Scoreboard()
r_paddle = Paddle(position=(350, 0))
l_paddle = Paddle(position=(-350, 0))


def start():
    scoreboard.seperator()
    ball.create_ball()
    screen.listen()
    game_is_on = True


start()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() > -330):
        ball.bounce_x()
        ball.bounce_y()

    # if paddle misses the ball
    if ball.xcor() > 395:
        ball.reset_position()
        scoreboard.lscore += 1
        scoreboard.refresh()

    if ball.xcor() < -395:
        scoreboard.rscore += 1
        scoreboard.refresh()
        ball.reset_position()
screen.exitonclick()
