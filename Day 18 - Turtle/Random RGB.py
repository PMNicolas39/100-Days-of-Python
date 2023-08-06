import turtle as t
import random


tim = t.Turtle()
t.colormode(255)
angle = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


tim.pensize(15)
tim.speed("normal")
step = 50

for _ in range(100):
    tim.color(random_color())
    tim.forward(step)
    tim.setheading(random.choice(angle))


screen = t.Screen()
screen.exitonclick()
