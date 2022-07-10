from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()

# change size of screen
screen.setup(width=500, height=400)

# add input
user_bet = screen.textinput(title= 'Make your bet', prompt='Which turtle will win the race? Enter a color: ')
# add rainbow color
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


# place 6 turtles with different colors at beginning of the race
# create empty list to append turtles instances with different state
all_turtles = []
# create a list of position on axis y and then distributed them to turtles
y_pos = [-70, -40, -10, 20, 50, 80]

# loop over to create turtles witch conditions set above
for i in range(6):
    new_tur = Turtle(shape="turtle")
    # new_tur.speed("fastest")
    new_tur.penup()
    new_tur.color(colors[i])
    new_tur.goto(x=-225, y=y_pos[i])
    all_turtles.append(new_tur)

# set condition to True so race will start
if user_bet:
    is_race_on = True


# do a while loop to iterate over all_turtles list
while is_race_on:

    for turtle in all_turtles:
        # 2. when turtle reach end of screen, race should stop
        if turtle.xcor() > 225:
            # 5. break loop to get winning_color prompt
            is_race_on = False
            winning_color = turtle.pencolor()
            # 3. check if winning color = user_bet
            if winning_color == user_bet:
                print(f"Congratulation! {winning_color} is the winner of the race!")
            else:
                print(f"You lose! {winning_color} is the winner of the race.")

    # 1. make them move at a different pace
        rand_pace = random.randint(0, 10)
        turtle.forward(rand_pace)


screen.exitonclick()

