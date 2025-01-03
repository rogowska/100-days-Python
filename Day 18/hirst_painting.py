import turtle as t
import random
import colorgram

palette = []

colors = colorgram.extract('Day 18\hirst.jpg', 15)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    palette.append((r,g,b))

#cleared out palette without background colors
palette = [(219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (245, 232, 236), (118, 82, 93), (179, 140, 150), (41, 46, 65), (162, 104, 151), (126, 173, 114), (83, 96, 183), (67, 9, 27), (238, 241, 245)]

t.colormode(255)
t.speed("fastest")
t.up()
t.hideturtle()

def make_dots(number_of_dots):
    for row in range(number_of_dots):
        t.teleport(x=0, y=50*row)
        for step in range(number_of_dots):
            t.dot(20, random.choice(palette))
            t.forward(50)

make_dots(5)
t.mainloop()