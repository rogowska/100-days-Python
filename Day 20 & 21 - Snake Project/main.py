from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from config import WIDTH, HEIGHT

game_on = True

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Left', fun=snake.turn_left)
screen.onkey(key='Right', fun=snake.turn_right)
screen.onkey(key='Up', fun=snake.go_up)
screen.onkey(key='Down', fun=snake.go_down)

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if food.distance(snake.return_head()) < 15:
        food.spawn()
        snake.grow()
        scoreboard.increase_score()
        
    #detect collision with wall
    if snake.return_head().xcor() > WIDTH/2 - 2 or snake.return_head().xcor() < -WIDTH/2 + 2 or snake.return_head().ycor() > HEIGHT/2 - 2 or snake.return_head().ycor() < -HEIGHT/2 + 2:
        game_on = False
        scoreboard.game_over()

    #detect collision with other segments
    for element in snake.snake_elements[1:]:
        if snake.head.distance(element) < 10:
            game_on = False
            scoreboard.game_over()


screen.mainloop()