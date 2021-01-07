from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.hideturtle()
        self.penup()
        self.pencolor("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.lvl}", align="left", font=FONT)

    def increase_level(self):
        self.lvl += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="left", font=FONT)
