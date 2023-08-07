# import colorgram
#
# rgb_color = []
# colors = colorgram.extract('dot.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     # create tuple
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)

import turtle as t
import random
import os

draw = t.Turtle()
t.colormode(255)
t.speed("fast")
draw.penup()
draw.hideturtle()

color_list = [(65, 154, 134), (132, 41, 43), (184, 98, 81), (183, 180, 181), (210, 200, 108), (178, 201, 186),
              (150, 180, 170), (90, 143, 158), (28, 81, 59), (193, 190, 192), (17, 78, 98),
              (215, 184, 172), (190, 190, 195), (78, 72, 31)]


def random_color():
    color = random.choice(color_list)
    return color


step = 50
dot = int(input("enter the number of dot: "))
col = int(input("enter the number of column: "))

for dot_count in range(1, dot+1):
    draw.dot(20, random_color())
    draw.forward(step)
    if dot_count % col == 0:
        draw.setheading(90)
        draw.forward(step)
        draw.setheading(180)
        draw.forward(step*col)
        draw.setheading(0)

screen = t.Screen()
screen.exitonclick()
