from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(-350)
r_paddle = Paddle(350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_over = False
while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top or bottom of screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with either paddle
    if (ball.xcor() < -320 and ball.distance(l_paddle) < 50) or (ball.xcor() > 320 and ball.distance(r_paddle) < 50):
        ball.x_bounce()

    # Detect if ball passes left paddle
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

    # Detect if ball passes right paddle
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_over = True
        scoreboard.game_over()

screen.exitonclick()
