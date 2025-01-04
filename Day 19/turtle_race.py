from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["plum", "tan", "salmon", "aquamarine", "peru", "maroon"]
turtles = []
y_pos = 100
is_race_on = True

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: (plum/tan/salmon/aquamarine/peru/maroon)")

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.teleport(x=-230, y=y_pos)
    turtle.up()
    y_pos -= 40
    turtles.append(turtle)

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_bet:
                print("You won,", turtle.pencolor(), "turtle won the race!")
            else:
                print("You lost,", turtle.pencolor(), "turtle won the race!")
            is_race_on = False
        turtle.forward(random.randint(0,10))

screen.mainloop()