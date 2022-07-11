from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.penup()
        # Circle is 20 by 20 pixel, we are reducing it by hal it's size, so 10 by 10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # To place the food randomly, we need to randomize x and y axis
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)

