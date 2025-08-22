from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

Y_POSITIONS = [260, 180, 100, 20, -60, -140, -220]
Y_RANDOM_POS_VARIATION = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

BASE_X = 260
BASE_Y = 260

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.goto(BASE_X, random.choice(Y_POSITIONS) + random.choice(Y_RANDOM_POS_VARIATION))
        # self.move()

    def move(self):
        self.penup()
        self.goto(self.xcor() - 20, self.ycor())

class CarManager:
    def __init__(self):
        self.car = Car()
        super().__init__()







