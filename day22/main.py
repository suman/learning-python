import time
from turtle import Screen
from player import Player
from car_manager import CarManager
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
game_is_on = True

screen.onkey(player.move, "Up")
screen.listen()

generate_car = True
all_cars = []

while game_is_on:
    time.sleep(player.speed)
    car_manager = CarManager()
    all_cars.append(car_manager.car)
    for car in all_cars:
        xcor = car.xcor()
        if player.distance(car) < 20: #game over
            player.game_over()
            game_is_on = False
        elif car.xcor() < -305: #remove the car which crosses the road
            all_cars.remove(car)
        else:
            car.move()
    screen.update()
screen.exitonclick()