from turtle import Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.title("Breakout-game")
screen.setup(width=1000, height=700)

paddle = Paddle((0,-300))

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

ball = Ball()

while True:
    ball.ball_move()

    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    if ball.ycor() > 330:
        ball.bounce_y()

    if ball.distance(paddle) < 40:
        ball.bounce_y()


screen.exitonclick()