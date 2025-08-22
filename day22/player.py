from turtle import Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
scorecard = Scoreboard()
class Player(Turtle):
    def __init__(self):
        self.speed = 0.5
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.tilt(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        ycor = self.ycor()

        self.penup()
        if ycor > FINISH_LINE_Y:
            scorecard.increase_score()
            self.speed += 0.05
            self.refresh()
        else:
            self.goto(self.xcor(), ycor + MOVE_DISTANCE)

    def game_over(self):
        scorecard.game_over()

    def refresh(self):
        self.goto(STARTING_POSITION)