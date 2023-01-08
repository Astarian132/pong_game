import turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=1200, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

player_1 = Paddle('player_1')
player_2 = Paddle('player_2')
score_1 = Scoreboard('player_1')
score_2 = Scoreboard('player_2')
ball = Ball()
screen.listen()

screen.onkeypress(player_1.go_up, "Up")
screen.onkeypress(player_1.go_down, "Down")
screen.onkeypress(player_2.go_up, "w")
screen.onkeypress(player_2.go_down, "s")

score_1.show_score()
score_2.show_score()

game_on = True
while game_on:
    ball.move()
    screen.update()
    time.sleep(0.05)
    if ball.xcor() > 320:
        if ball.detect_paddle(player_1) == False:
            score_2.goal()
            ball.reset_position()

    if ball.xcor() < -320:
        if ball.detect_paddle(player_2) == False:
            score_1.goal()
            ball.reset_position()

screen.exitonclick()
