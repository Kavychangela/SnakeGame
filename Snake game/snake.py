from turtle import Turtle

pos = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in pos:
            self.add_segment(position)

    def add_segment(self, position):
        timmy = Turtle("square")
        timmy.color("white")
        timmy.penup()
        timmy.goto(position)
        self.segments.append(timmy)

    def extend(self):
        last_segment = self.segments[-1]
        self.add_segment(last_segment.position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)