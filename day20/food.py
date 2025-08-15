from score_card import Turtle
import random

class Food(Turtle):
    def __init__(self) :
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

