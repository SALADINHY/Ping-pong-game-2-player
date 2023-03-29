from traceback import print_tb
from turtle import Screen,Turtle, width
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=800)
screen.bgcolor("black")
screen.title("Pong Game Challenge")
screen.tracer(0)
player1=Paddle((0,350));
player2=Paddle((0,-350));
ball=Ball()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(player1.left,"Left")
screen.onkey(player1.right,"Right")
screen.onkey(player2.left,"a")
screen.onkey(player2.right,"d")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()
    if ball.xcor()>280 or ball.xcor()<-280:
        ball.naybatx()
    if ball.distance(player1)<50 and ball.ycor()>320 or ball.distance(player2)<50 and ball.ycor()<-320:
        ball.naybaty()
    if ball.ycor()>380:
        ball.refresh()
        scoreboard.p2_point()
    if ball.ycor()<-380:
        ball.refresh()
        scoreboard.p1_point()
    if scoreboard.p1_score == 10 and scoreboard.p2_score < 10:
        print("Player 1 is winner")
        scoreboard.check_winer()
        game_is_on=False
    elif scoreboard.p2_score == 10 and scoreboard.p1_score < 10:
        print("Player 2 is winner")
        scoreboard.check_winer()
        game_is_on=False
screen.exitonclick()