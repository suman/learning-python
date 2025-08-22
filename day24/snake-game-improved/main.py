from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from score_card import Scorecard

score_card = Scorecard()
screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
game_continue = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
snake_food = Food()

while game_continue:
    screen.update()
    time.sleep(0.2)
    snake.move()
    snake.head.shape()
    distance = snake.head.distance(snake_food)

    # eat food
    if distance < 15:
        snake_food.refresh()
        score_card.increase_score()
        snake.extend_segment()

    # collision on wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_continue = False
        snake.reset()
        score_card.game_over()
        score_card.game_over()

    # collision on body part
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_continue = False
            score_card.game_over()

screen.exitonclick()