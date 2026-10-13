from turtle import Screen
import turtle
import time
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard

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


msg = turtle.Turtle()
msg.hideturtle()
msg.penup()
msg.color("red")



for row in range(5):
    for col in range(9):
        x = -400 + col * 100
        y = 250 - row * 50
        brick = Brick((x, y))

        bricks.append(brick)

keep_playing = True

scoreboard = Scoreboard()

while keep_playing:
    ball.ball_move()
    screen.update()
    time.sleep(0.05)

    if ball.xcor() > 480 or ball.xcor() < -480:
        ball.bounce_x()

    if ball.ycor() > 330:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.y_move < 0:
        ball.bounce_y()

    for brick in bricks[:]:
        x_distance = abs(ball.xcor() - brick.xcor())
        y_distance = abs(ball.ycor() - brick.ycor())
        if ball.distance(brick) < 40:
            if y_distance < x_distance:
                ball.bounce_x()
            else:
                ball.bounce_y()
            brick.hideturtle()
            bricks.remove(brick)
            scoreboard.increase_score()
            break

    if len(bricks) == 0:
        keep_playing = False
        result = "win"


    elif ball.ycor() < -330:
        keep_playing = False
        result = "lose"


if result == "win":
    msg.color("green")
    msg.write(f"YOU WON!\nYour final score is: {scoreboard.score}", align="center", font=("Arial", 24, "bold"))

elif result == "lose":
    msg.color("red")
    msg.write(f"YOU LOST!\nYour final score is: {scoreboard.score}", align="center", font=("Arial", 24, "bold"))


screen.exitonclick()