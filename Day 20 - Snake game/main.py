import time
from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake game")
screen.setup(width=500, height=500)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()


screen.exitonclick()
