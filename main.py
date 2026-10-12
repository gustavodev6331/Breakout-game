from turtle import Screen
import turtle
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

l_msg = turtle.Turtle()
l_msg.hideturtle()
l_msg.penup()
l_msg.color("red")

v_msg = turtle.Turtle()
v_msg.hideturtle()
v_msg.penup()
v_msg.color("green")


for row in range(5):
    for col in range(9):
        x = -400 + col * 100
        y = 250 - row * 50
        brick = Brick((x, y))

        bricks.append(brick)

keep_playing = True

while keep_playing:
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

    if len(bricks) == 0:
        keep_playing = False
        l_msg.goto(0, 0)
        l_msg.write(
            "YOU WON!",
            align="center",
            font=("Arial", 24, "bold"),
        )


    if ball.ycor() < -330:
        keep_playing = False

        l_msg.goto(0, 0)
        l_msg.write(
            "YOU LOST!",
            align="center",
            font=("Arial", 24, "bold"),
        )

screen.exitonclick()