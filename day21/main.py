# Create Pong Screen
# create computer paddle and move
# create end user paddle and move
# Create ball and move
# Detect ball collision with paddle
# Update scorecard if ball does not collision with paddle
# Move the ball opposite side of screen if it collides with the bal
# Game over once the score is reached to 10

from turtle import Turtle, Screen
from scorecard import Scorecard
from ball import Ball
import time
WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

from screen_border import ScreenBorder
from paddle import Paddle

ScreenBorder(HEIGHT)
left_paddle = Paddle(WIDTH, HEIGHT, 'left')
right_paddle = Paddle(WIDTH, HEIGHT, 'right')

right_score_position = (WIDTH / 4), (HEIGHT/ 2 ) - 30
right_score = Scorecard(right_score_position)

left_score_position = (-(WIDTH / 4)), (HEIGHT/ 2 ) - 30
left_score = Scorecard(left_score_position)

pong_ball = Ball()

screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')

screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')

game_continue = True
screen.listen()
while game_continue:
    print('pong ball speed ', pong_ball.move_speed)
    time.sleep(0.1)
    screen.update()
    pong_ball.move()

    #if top wall hits
    if pong_ball.ball.ycor() > 290 or pong_ball.ball.ycor() < -290:
        pong_ball.bounce_y()

    right_paddle_distance = pong_ball.ball.distance(right_paddle.head)
    left_paddle_distance = pong_ball.ball.distance(left_paddle.head)

    if right_paddle_distance < 30 or left_paddle_distance < 30:
        pong_ball.bounce_x()

    if pong_ball.ball.xcor() > 380:
        left_score.increase_score()
        pong_ball.reset_position()

    if pong_ball.ball.xcor() < -380:
        right_score.increase_score()
        pong_ball.reset_position()

screen.exitonclick()