from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
from menu import Menu
import time

scr = Screen()
scr.setup(width=800, height=600)
scr.bgcolor('black')
scr.title('Pong')
scr.tracer(0)

l_pad = Paddle((-350, 0))
r_pad = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

game_state = "running"

def play_pause_game():
    global game_state
    if game_state == "paused":
        game_state = "running"
        menu.play_pause_btn.set_text("Pause")
    elif game_state == "running":
        game_state = "paused"
        menu.play_pause_btn.set_text("Resume")

def quit_game():
    global game_on
    game_on = False
    scr.bye()

def restart_game():
    global game_state
    ball.reset_pos()
    game_state = "running"
    score.score_reset()
    l_pad.update_paddle_pos((-350, 0))
    r_pad.update_paddle_pos((350, 0))
    menu.play_pause_btn.set_text("Pause")

menu = Menu(play_pause_game, quit_game, restart_game)

scr.listen()
scr.onkeypress(r_pad.pressed_up, 'Up')
scr.onkeyrelease(r_pad.released_up, 'Up')

scr.onkeypress(r_pad.pressed_down, 'Down')
scr.onkeyrelease(r_pad.released_down, 'Down')

scr.onkeypress(l_pad.pressed_up, 'w')
scr.onkeyrelease(l_pad.released_up, 'w')

scr.onkeypress(l_pad.pressed_down, 's')
scr.onkeyrelease(l_pad.released_down, 's')
    
game_on = True
while game_on:
    scr.update()
    if game_state == 'running':
        time.sleep(ball.fast)
        ball.move()
        l_pad.up()
        l_pad.down()
        r_pad.up()
        r_pad.down()
        if ball.ycor() >= 290 or ball.ycor() <= -290:
            ball.bounce_y()

        if abs(ball.xcor() - r_pad.xcor()) < 20 and abs(ball.ycor() - r_pad.ycor()) < 55:
            ball.bounce_x()
            
        if abs(ball.xcor() - l_pad.xcor()) < 20 and abs(ball.ycor() - l_pad.ycor()) < 55:
            ball.bounce_x()
        
        if ball.xcor() >= 395:
            ball.reset_pos()
            score.l_increment()
            
        if ball.xcor() <= -395:
            ball.reset_pos()
            score.r_increment()

scr.exitonclick()