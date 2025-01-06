from turtle import Screen, Turtle
import time
from snake import Snake

game_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
screen.mainloop()