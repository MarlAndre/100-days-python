import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# 1. Turn off animation
screen.tracer(0)

snake = Snake()

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


screen.exitonclick()
