import turtle as t
import random

tim = t.Turtle()
colors = ["RoyalBlue", "MediumSpringGreen", "Brown", "Magenta", "Linen", "Goldenrod	"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(50)
        tim.right(angle)


for side in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(side)

screen = t.Screen()
screen.exitonclick()