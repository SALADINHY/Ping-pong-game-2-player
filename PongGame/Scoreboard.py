from turtle import Turtle, update
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_board()
    def update_board(self):
        self.clear()
        self.goto(270,50)
        self.write(self.p1_score,align="center",font=("Arial",50,"normal"))
        self.goto(270,-50)
        self.write(self.p2_score,align="center",font=("Arial",50,"normal"))
    def p1_point(self):
        self.p1_score+=1
        self.update_board()
    def p2_point(self):
        self.p2_score+=1
        self.update_board()
    def check_winer(self):
        self.goto(0,0)
        self.write("End Game",align="center",font=("Arial",50,"normal"))