import random
from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=500, height=500)
user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a colour: ")
y_direction = [100, 50, 0, -50, -100]
colors = ['blue', 'green', 'red', 'black', 'cyan']

new_turtle = []
for i in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-250, y=y_direction[i])
    new_turtle.append(tim)

is_game_over = True
while is_game_over:
    for turtles in new_turtle:
        step = random.randint(0, 10)
        turtles.forward(step)
        if turtles.xcor() == 0:
            is_game_over = False
            winner = turtles.pencolor()
            if winner == user_bet:
                print(f"you won, winner is: {winner} turtle")
            else:
                print(f"you lost, winner is: {winner} turtle")














screen.exitonclick()
