from turtle import Screen
from config import WIDTH, HEIGHT
from paddle import Paddle

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_paddle = Paddle()

screen.listen()

screen.mainloop()