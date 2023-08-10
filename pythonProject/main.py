import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=300, height=300)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = []
x_direction = [(0, 0), (-20, 0), (-40, 0)]
for i in x_direction:
    tim = Turtle(shape="square")
    tim.penup()
    tim.color("white")
    tim.goto(i)
    snake.append(tim)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for snake_seg in snake:
        snake_seg.forward(20)


screen.exitonclick()
