from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.goto(0, 270)
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.write(f'Score: {self.score}', font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', font=FONT, align=ALIGNMENT)


    def increase_score(self):
        self.score_update()
        self.clear()
        self.score += 1
