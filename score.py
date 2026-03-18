from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-150, 240)
        self.write(self.l_score, align='center', font=("Trebuchet MS", 25, 'bold'))
        self.goto(150, 240)
        self.write(self.r_score, align='center', font=("Trebuchet MS", 25, 'bold'))
        self.goto(0, 245)
        self.write("PONG", align='center', font=("Trebuchet MS", 36, 'bold'))

    def update(self):
        self.clear()
        self.goto(-150, 250)
        self.write(self.l_score, align='center', font=("Trebuchet MS", 25, 'bold'))
        self.goto(150, 250)
        self.write(self.r_score, align='center', font=("Trebuchet MS", 25, 'bold'))
        self.goto(0, 245)
        self.write("PONG", align='center', font=("Trebuchet MS", 36, 'bold'))


    def r_increment(self):
        self.r_score += 1
        self.update()

    def l_increment(self):
        self.l_score += 1
        self.update()

    def score_reset(self):
        self.r_score = 0
        self.l_score = 0
        self.update()

