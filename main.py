from turtle import Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.title("Breakout-game")
screen.setup(width=1000, height=700)

paddle = Paddle((0,-250))

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

ball = Ball()

while True:
    ball.ball_move()




screen.exitonclick()