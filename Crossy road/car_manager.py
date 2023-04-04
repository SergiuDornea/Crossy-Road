COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
from turtle import Turtle
# 20 * 40 px
class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(x=300, y=random.randint(-250, 250))
            new_car.left(180)
            self.cars.append(new_car)

    def move_car(self):
       for car in self.cars:
           car.forward(self.car_speed)



    def move_car_faster(self):
        self.car_speed += MOVE_INCREMENT





