from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.penup()
        self.goto(position)
        self.keys = {'Up' :False, 'Down': False}

    def pressed_up(self): self.keys['Up'] = True
    def released_up(self): self.keys['Up'] = False
   
    def pressed_down(self): self.keys['Down'] = True
    def released_down(self): self.keys['Down'] = False


    def up(self):
        if self.ycor() <= 235 and self.keys['Up']:
            new_cor = self.ycor() + 20
            self.goto(self.xcor(), new_cor)

    def down(self):
        if self.ycor() >= -235 and self.keys['Down']:
            new_cor = self.ycor() - 20
            self.goto(self.xcor(), new_cor)
    def update_paddle_pos(self, new_position):
        self.goto(new_position)

