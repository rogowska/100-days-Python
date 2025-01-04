import turtle

def forward():
    t.fd(10)

def backward():
    t.bk(10)

def left():
    t.lt(10)

def right():
    t.rt(10)

def clear():
    turtle.resetscreen()

t = turtle.Turtle()
screen = turtle.Screen()

screen.listen()

screen.onkey(key='a', fun=left)
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key='d', fun=right)
screen.onkey(key='c', fun=clear)

screen.mainloop()