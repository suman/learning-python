from turtle import Turtle

ALIGNMENT = "center"
FONTSTYLE = ("Arial", 20, "bold")


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor('white')
        self.penup()
        self.setheading(90)
        self.forward(270)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONTSTYLE)
        self.speed("fastest")

    def update_score(self):
        self.clear()
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONTSTYLE)
        return self.score

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONTSTYLE)