FONT = ("Courier", 24, "normal")
from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("black")
        self.goto(x=-290, y=260)
        self.write_score()

    def write_score(self):
        self.pencolor("black")
        self.write(f"Level: {self.score}", font=FONT)

    def delete_score(self):
        self.pencolor("white")
        self.write(f"Level: {self.score}", font=FONT)

    def point(self):
        self.score += 1
        self.clear()
        self.write_score()


    def game_over(self):
        self.goto(x=-80, y=0)
        self.write("GAME OVER", font= FONT)
