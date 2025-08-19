from turtle import Turtle

class ScreenBorder():
    def __init__(self, height):
        self.squares = []
        self.height = height
        for i in range(30):
            turtle = Turtle('square')
            turtle.speed("fastest")
            if (i + 1) % 2 == 0:
                turtle.color('black')
                turtle.fillcolor('black')
            else:
                turtle.color('white')
                turtle.fillcolor('white')
            turtle.width(20)
            turtle.penup()
            turtle.goto(-5, (self.height / 2) - ( (i + 1) * 20))
            self.squares.append(turtle)