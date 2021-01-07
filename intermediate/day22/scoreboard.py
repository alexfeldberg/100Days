from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-210, 250)
        self.write(self.l_score, align="center", font=("Courier", 30, "normal"))
        self.goto(190, 250)
        self.write(self.r_score, align="center", font=("Courier", 30, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
