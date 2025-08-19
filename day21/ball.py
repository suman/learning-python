from turtle import Turtle

class Ball():
    def __init__(self):
        self.ball = Turtle('circle')
        self.ball.pencolor("white")
        self.ball.fillcolor("red")
        self.ball.shapesize(1)
        self.y_move = 3
        self.x_move = 3
        self.move_speed = 0.1

    def move(self):
        self.ball.penup()
        # self.ball.forward(20)
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        print("reset position")
        self.ball.goto(0, 0)
        self.ball.move_speed = 0.1

