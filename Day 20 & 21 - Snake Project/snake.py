from turtle import Turtle

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SPEED = 20
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self):
        self.snake_elements = []
        self.create_snake()
        self.head = self.snake_elements[0]

    def create_snake(self):
        '''Create starter snake made of three elements'''
        for position in STARTING_POSITIONS:
            self.add_element(position)
        
    def add_element(self, position):
        '''Add element to the snake'''
        new_snake_element = Turtle(shape="square")
        new_snake_element.color("white")
        new_snake_element.up()
        new_snake_element.goto(position)
        self.snake_elements.append(new_snake_element)

    def grow(self):
        '''Add element to the snake after eating food'''
        self.add_element(self.snake_elements[-1].position())

    def move(self):
        '''Move the snake by one unit'''
        for idx in range(len(self.snake_elements)-1, 0, -1):
            new_x = self.snake_elements[idx-1].xcor()
            new_y = self.snake_elements[idx-1].ycor()
            self.snake_elements[idx].goto(new_x, new_y)
        self.head.forward(SPEED)

    def return_head(self):
        '''Return head element of snake'''
        return self.head

    def turn_left(self):
        '''Turn the snake left'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def turn_right(self):
        '''Turn the snake right'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_up(self):
        '''Turn the snake to go up'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        '''Turn the snake to go down'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)