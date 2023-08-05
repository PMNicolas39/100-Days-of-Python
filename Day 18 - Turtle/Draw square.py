from turtle import Turtle, Screen

line = Turtle()
line.shape("arrow")
line.color("black")

# run 4 times
for _ in range(4):
    line.forward(100)
    line.right(90)
    # line.forward(100)
