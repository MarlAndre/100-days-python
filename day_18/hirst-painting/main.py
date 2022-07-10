import turtle as t
import random
# import colorgram

# Extract 30 colors from image
# colors = colorgram.extract('1200x878.jpg', 30)
# color_palette = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color = (r, g, b)
#     color_palette.append(rgb_color)
# print(color_palette)

# copy/paste result here
color_list = [(220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222), (203, 134, 157), (180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52), (213, 87, 61), (197, 85, 112), (208, 223, 231), (229, 199, 114), (57, 166, 135), (141, 33, 42), (8, 104, 80), (47, 158, 182), (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157), (126, 38, 34), (156, 210, 197), (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47)]

# create 10 by 10 dot painting
t.colormode(255)
paint = t.Turtle()
paint.speed("fastest")


def draw_painting(space, dots):
    for i in range(dots):
        for y in range(dots):
            paint.dot(10, random.choice(color_list))
            paint.forward(space)

        paint.backward(space * dots)
        paint.left(90)
        paint.forward(space)
        paint.right(90)


paint.penup()
draw_painting(30, 10)


screen = t.Screen()
screen.exitonclick()
