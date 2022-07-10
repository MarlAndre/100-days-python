from turtle import Turtle, Screen
import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# TODO 1 draw shape and change color at each new shape
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_num_side in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_num_side)


# TODO 2 draw a random walk, change color each direction and make it go faster
# direction are nort, east, south and west
# directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# TODO 3 draw a circle and make a spirograph
# First spirograph
# for _ in range(20):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.left(100)


# Second spirograph
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(8)

screen = Screen()
screen.exitonclick()
