from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
game_continue = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_continue:
    screen.update()
    time.sleep(0.5)
    snake.move()

screen.exitonclick()