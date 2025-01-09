from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.score=0
        self.write(arg=f"Score:{self.score} ", align="center", font=("Arial", 16, "normal"))

    def increase_score(self):
        self.score+=1
        self.write(arg=f"Score:{self.score} ", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Gameover ", align="center", font=("Arial", 16, "normal"))

