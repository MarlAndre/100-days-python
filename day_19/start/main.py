from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# TODO 1 make an etch and sketch game
# w = forwards, s = backwards, a = counter-clockwise, d = clockwise, c = clear

# tim.setpos(0.00, 0.00)


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def move_counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_board():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
# w = forwards
screen.onkey(key="w", fun=move_forwards)
# s = backwards
screen.onkey(key="s", fun=move_backwards)
# a = counter-clockwise
screen.onkey(key="a", fun=move_counter_clockwise)
# d = clockwise
screen.onkey(key="d", fun=move_counter_clockwise)
# c = clear
screen.onkey(key="c", fun=clear_board)

screen.exitonclick()