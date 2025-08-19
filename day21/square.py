from turtle import Turtle, Screen

class Square(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.pencolor("white")
        self.fillcolor("white")
