import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# 1. Turn off animation
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')



game_is_on = True

while game_is_on:
    # 1. After each segment move, update screen
    screen.update()
    # 1. Will delay by x sec after the whole body moved
    time.sleep(0.1)
    snake.move()
    scoreboard.score_update()

    # Detect collision with food. To do this, we use the first segment of the snake(head)
    # if the segment is in a distance of less than 15 pixel from food, they collide
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.score_update()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    # If head collide with segment in body and tail, game_over


screen.exitonclick()
