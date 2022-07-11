from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.goto(0, 270)
        self.score = 0
        self.color('white')
        self.hideturtle()

    def score_update(self):
        self.write(f'Score: {self.score}', font=('Arial', 16, 'normal'), align='center')
