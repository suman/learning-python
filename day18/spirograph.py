import random
from turtle import Turtle, Screen
timmy_turtle = Turtle()
timmy_turtle.shape('turtle')
colors = ["red", "green", "blue", "yellow"]
direction = [0, 90, 180, 360]

timmy_turtle.pensize(5)
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = ( r, g, b)
    print(rgb)
    return rgb

def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy_turtle.speed("fastest")
        pick_color = random_color()
        timmy_turtle.pencolor(random_color())
        timmy_turtle.circle(70)
        timmy_turtle.setheading(timmy_turtle.heading() + 10)

draw_spirograph(10)
screen.exitonclick()