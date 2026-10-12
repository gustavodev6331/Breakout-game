from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from brick import Brick

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Breakout-game")
screen.setup(width=1000, height=700)

paddle = Paddle((0,-300))

screen.listen()
screen.onkey(paddle.left, "Left")
screen.onkey(paddle.right, "Right")

ball = Ball()

bricks = []

for row in range(5):
    for col in range(9):
        x = -400 + col * 100
        y = 250 - row * 50
        brick = Brick((x, y))

        bricks.append(brick)




while True:
    ball.ball_move()
    screen.update()
    time.sleep(0.05)

    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    if ball.ycor() > 330:
        ball.bounce_y()

    if ball.distance(paddle) < 50:
        ball.bounce_y()

    for brick in bricks[:]:
        if ball.distance(brick) < 20:
            brick.hideturtle()
            bricks.remove(brick)
            ball.bounce_y()
            break



screen.exitonclick()