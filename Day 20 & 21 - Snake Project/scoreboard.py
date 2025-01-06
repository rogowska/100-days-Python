from turtle import Turtle
from config import WIDTH, HEIGHT

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.score = 0
        self.display_score()

    def display_score(self):
        '''Refresh the board and display the score'''
        self.clear()
        self.teleport(-10, HEIGHT/2.5)
        text = "Score: " + str(self.score)
        self.write(text, align = "center", font=('Arial', 12, 'normal'))

    def increase_score(self):
        '''Increase score by one'''
        self.score += 1