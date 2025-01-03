import turtle as t
import random

t.colormode(255)

def draw_shape(sides_number):
    for step in range(sides_number):
        t.forward(100)
        t.right(360/sides_number)

for number in range(3, 11):
    t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    draw_shape(number)

t.mainloop()