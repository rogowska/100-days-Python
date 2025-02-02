import turtle as t
import random

t.colormode(255)
t.pensize(5)
t.speed(10)

def random_walk():
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    t.forward(20)
    direction = [0, 90, 180, 270]
    t.setheading(random.choice(direction))

for _ in range(50):
    random_walk()

t.mainloop()