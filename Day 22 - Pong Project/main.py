from turtle import Screen
from config import WIDTH, HEIGHT

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.mainloop()