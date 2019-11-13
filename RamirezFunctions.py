#function file
import turtle
bob = turtle.Turtle()

def polygon(sides,distance,c):
    bob.begin_fill()
    bob.color(c)
    angle = 360/sides
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(distance,c):
    bob.begin_fill()
    bob.color(c)
    for times in range(5):
        bob.forward(distance)
        bob.right(144)
    bob.end_fill()

def explosion(d,c):
    bob.color(c)
    for times in range(8):
        bob.forward(d)
        bob.right(135)

def circle(d,c):
    bob.begin_fill()
    bob.color(c)
    bob.circle(a)
    bob.end_fill()



