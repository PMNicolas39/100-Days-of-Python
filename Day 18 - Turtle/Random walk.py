import turtle as t
import random

color = ["RoyalBlue", "MediumSpringGreen", "Brown", "Magenta", "Linen", "Goldenrod"]
angle = [0, 90, 180, 270]

tim = t.Turtle()
tim.pensize(15)
tim.speed("normal")
step = 50

for _ in range(100):
    tim.color(random.choice(color))
    tim.forward(step)
    tim.setheading(random.choice(angle))


screen = t.Screen()
screen.exitonclick()
