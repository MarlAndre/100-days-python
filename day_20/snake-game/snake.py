from turtle import Turtle
PACE = 20
UP = 90
RIGHT = 0
DOWN = 270
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_body()
        self.head = self.snake_body[0]

# Create initial body
    def create_body(self):
        for i in range(3):
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            x_offset = -20 * len(self.snake_body)
            snake_segment.goto(x_offset, 0)
            self.snake_body.append(snake_segment)

# Make snake move
    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(PACE)

    def up(self):
        # If snake is going down, he can't go up, so user have to use left or right key to move snake
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)



