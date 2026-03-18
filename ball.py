from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.move_x = 10
        self.move_y = 10
        self.fast = 0.05
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1 

    def bounce_x(self):
        self.move_x *= -1 
        self.fast *= 0.9
        if self.move_x > 0:
            self.setx(self.xcor() + 10)
        else:
            self.setx(self.xcor() - 10)


    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()
        self.fast = 0.05