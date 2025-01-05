from turtle import Screen, Turtle
import time

ELEMENT_WIDTH = 20

game_on = True
snake_elements = []
speed = ELEMENT_WIDTH*1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#INITIALIZATION OF SNAKE
for pos in range(3):
    new_snake_element = Turtle(shape="square")
    new_snake_element.color("white")
    new_snake_element.up()
    new_snake_element.setx(0 - pos*ELEMENT_WIDTH)
    snake_elements.append(new_snake_element)

while game_on:
    screen.update()
    time.sleep(0.5)
    for idx in range(len(snake_elements)-1, 0, -1):
        snake_elements[idx].teleport(snake_elements[idx-1].xcor(), snake_elements[idx-1].ycor())
    snake_elements[0].forward(speed)

screen.mainloop()