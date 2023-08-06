import turtle as t
import random

draw = t.Turtle()
draw.pensize(2)
t.colormode(255)
t.speed("fast")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for angle in range(0, 360, 20):
    draw.color(random_color())
    draw.setheading(angle)
    draw.circle(20)


screen = t.Screen()
screen.exitonclick()
