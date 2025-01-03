import turtle as t
import random

t.colormode(255)
t.speed("fastest")

def draw_spriograph(density):
    for _ in range(density):
        t.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.circle(radius=100, steps=1000)
        t.left(360/density)

draw_spriograph(10)
t.mainloop()