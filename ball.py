from turtle import Turtle
import random

start_ball_move = [(10, 10), (-10, 10)]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(x=0, y=-250)


        self.x_move, self.y_move = random.choice(start_ball_move)

    def ball_move(self):
        new_x= self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1
