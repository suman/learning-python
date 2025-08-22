from turtle import Turtle

ALIGNMENT = "center"
FONTSTYLE = ("Arial", 20, "bold")

Y_COR_START = 270
# high_score = 0
# file = open('high_score.txt', 'r+')

with open("high_score.txt", "r") as file:
    # Write the new content to the file
    high_score = file.read()

# high_score = file.read()
if high_score is None:
    high_score = 0
else:
    high_score = int(high_score)

class Score(Turtle):
    def __init__(self, score_type):
        super().__init__()
        if score_type == 'Score':
            self.score = 0
        else:
            self.score = high_score

        self.score_type = score_type
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.setheading(90)
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()


    def update_score(self):
        self.clear()
        if self.score_type == 'Score':
            self.goto(-80, Y_COR_START)
        else:
            self.goto(80, Y_COR_START)

        self.write(f"{self.score_type} = {self.score}", align=ALIGNMENT, font=FONTSTYLE)

        self.write(f"{self.score_type} = {self.score}", align=ALIGNMENT, font=FONTSTYLE)

    def reset_score(self):
        self.score = 0
        self.update_score()


class Scorecard:
    def __init__(self):
        self.score = Score('Score')
        self.high_score = Score('High Score')

        # self.total_score =  self.score.score
        # self.total_high_score = self.high_score.score


    def increase_score(self):
        self.score.increase_score()

    def game_over(self):
        if self.score.score > self.high_score.score:
            self.high_score.score = self.score.score
        self.high_score.update_score()
        with open("high_score.txt", "w") as file_h:
            # Write the new content to the file
            file_h.write(f'{self.high_score.score}\n')
        self.score.reset_score()

