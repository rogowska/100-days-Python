from turtle import Turtle
import random
from config import WIDTH, HEIGHT

class Food(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.color("pink")
        self.resizemode("user")
        self.shapesize(0.5,0.5)
        self.spawn()
    
    def spawn(self):
        '''Spawn food in the random place on screen'''
        random_x = random.randrange(-int(WIDTH/2 - 15), int(WIDTH/2 - 15))
        random_y = random.randrange(-int(HEIGHT/2 - 15), int(HEIGHT/2 - 15))
        self.teleport(random_x, random_y)
        