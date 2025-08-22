from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.display_score()

    def display_score(self):
        self.color("black")
        self.penup()
        self.goto(-130, 270)
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)


    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.color("black")
        self.penup()
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)

