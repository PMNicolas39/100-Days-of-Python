from turtle import Turtle

body = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
Up = 90
Down = -90
Left = 180
Right = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.body_snake()
        self.head = self.segment[0]

    def body_snake(self):
        for i in body:
            self.add_segment(i)

    def add_segment(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segment.append(tim)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        # forward function
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        self.head.setheading(Up)

    def down(self):
        self.head.setheading(Down)

    def left(self):
        self.head.setheading(Left)

    def right(self):
        self.head.setheading(Right)
