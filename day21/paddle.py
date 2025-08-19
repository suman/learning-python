import turtle
from turtle import Turtle
MOVE_DISTANCE = 20
class Paddle:

    def __init__(self, width, height, paddle_type):
        self.height = height
        self.width = width
        self.head = ""
        self.paddle_start = False
        position_start_y = 0
        if paddle_type == "left":
            self.display_paddle(-((self.width / 2) - 30), position_start_y)
        else:
            self.display_paddle((self.width / 2) - 30, position_start_y)

    def display_paddle(self, x_start, y_start):
        paddle = Turtle('square')
        paddle.color("white")
        paddle.fillcolor('white')
        paddle.shapesize(stretch_wid= 5, stretch_len=1)
        paddle.penup()
        paddle.goto(x_start, y_start)
        self.head = paddle

    def move_up(self):
        new_y = self.head.ycor() + 20
        x = self.head.xcor()
        if self.head.ycor() < 290:
            self.head.goto(x, new_y)

    def move_down(self):
        # print("Pressed down key")
        new_y = self.head.ycor() - 20
        x = self.head.xcor()
        if self.head.ycor() > -290:
            self.head.goto(x, new_y)

