import turtle
import random
Tony = turtle.Turtle()
Tony.color('red','green')
Tony.width(10)


Tony.begin_fill()
Tony.circle(100)
Tony.end_fill()

Tony.penup()
Tony.forward(100)
Tony.pendown()

Tony.color('gray','crimson')
Tony.begin_fill()
for i in range(5):
