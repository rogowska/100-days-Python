from turtle import Turtle
from config import HEIGHT

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.teleport(0, HEIGHT/2.5)
        self.score = 0
        self.display_score()

    def display_score(self):
        '''Refresh the board and display the score'''
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        '''Increase score by one'''
        self.score += 1
        self.display_score()

    def game_over(self):
        '''Write game over text'''
        self.teleport(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)