from turtle import Turtle
from config import WIDTH

class Paddle(Turtle):

    def __init__(self):
        super().__init__(shape="square")
        self.color("pink")
        self.resizemode("user")
        self.shapesize(5,15)
        self.up()
        self.spawn()
    
    def spawn(self):
        self.goto(0, -WIDTH+10)