from turtle import Turtle, Screen
from screen_border import ScreenBorder
from paddle import Paddle

WIDTH = 800
HEIGHT = 600
STARTING_POSITION = [(-10, (HEIGHT / 2) - 60)]


class PongScreen():
    def __init__(self):
        ScreenBorder(HEIGHT)
        computer_paddle = Paddle(WIDTH, HEIGHT, 'computer')
        user_paddle = Paddle(WIDTH, HEIGHT, 'user')
