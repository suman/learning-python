from turtle import Turtle

POSITIONS = [(0, 0), (-20, -0), (-40, -0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.squares = []
        self.snake_width = 20
        self.positions = POSITIONS
        self.draw_snake()

    def draw_snake(self):
        for position in self.positions:
            square = Turtle()
            square.shape("square")
            square.color("white")
            square.width(self.snake_width)
            square.penup()
            square.goto(position)
            self.squares.append(square)

    def move(self):
        for seg_num in range(len(self.squares) - 1, 0, -1):
            x = self.squares[seg_num - 1].xcor()
            y = self.squares[seg_num - 1].ycor()
            self.squares[seg_num].goto(x, y)
        self.squares[0].forward(20)

    def up(self):
        if not self.squares[0].heading() == DOWN:
            self.squares[0].setheading(UP)

    def down(self):
        if not self.squares[0].heading() == UP:
            self.squares[0].setheading(DOWN)

    def right(self):
        if not self.squares[0].heading() == LEFT:
            self.squares[0].setheading(RIGHT)

    def left(self):
        if not self.squares[0].heading() == RIGHT:
            self.squares[0].setheading(LEFT)
