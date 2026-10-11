from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.title("Breakout-game")
screen.setup(width=800, height=600)

paddle = Paddle((0,-260))

screen.listen()

screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

screen.exitonclick()