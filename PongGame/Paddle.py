from turtle import Turtle, position
import turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.rt(90)
        self.shapesize(stretch_wid=5,stretch_len=1)
    def left(self):
        new_x = self.xcor()-50
        self.goto(new_x,self.ycor())
    def right(self):
        new_x = self.xcor()+50
        self.goto(new_x,self.ycor())

