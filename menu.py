from turtle import Turtle

class Button(Turtle):
    def __init__(self, text, position, action):
        super().__init__()

        self.penup()
        self.goto(position)
        self.action = action
        self.text = text

        self.shape("square")
        self.shapesize(1,4)
        self.fillcolor("white")
        self.showturtle()

        self.label = Turtle()
        self.label.hideturtle()
        self.label.penup()
        self.label.color("white")
        self.label.goto(position[0], position[1] + 10)
        self.label.write(self.text, align='center', font=("Arial", 12, 'bold'))

        self.onclick(self.clicked)
    
    def set_text(self,new_text):
        self.text = new_text
        self.label.clear()
        self.label.write(self.text, align='center', font=("Arial", 12, 'bold'))

    def clicked(self,  x, y):
        self.action()
    
class Menu():
    def __init__(self, play_pause, quit, restart):
        self.play_pause_btn = Button("Pause", (-90, -275), play_pause)
        self.restart_btn = Button("Restart", (0, -275), restart)
        self.quit_btn = Button("Quit", (90, -275), quit)