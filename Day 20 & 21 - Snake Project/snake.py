from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SPEED = 20

class Snake:

    def __init__(self):
        self.snake_elements = []
        self.create_snake()
        self.head = self.snake_elements[0]

    def create_snake(self):
            for pos in range(3):
                new_snake_element = Turtle(shape="square")
                new_snake_element.color("white")
                new_snake_element.up()
                new_snake_element.setx(0 - pos*SPEED)
                self.snake_elements.append(new_snake_element)
        
    def move(self):
        for idx in range(len(self.snake_elements)-1, 0, -1):
            self.snake_elements[idx].goto(self.snake_elements[idx-1].xcor(), self.snake_elements[idx-1].ycor())
        self.head.forward(SPEED)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)