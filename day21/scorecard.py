from turtle import Turtle


class Scorecard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.pencolor('white')
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))
