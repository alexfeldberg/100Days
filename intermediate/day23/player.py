from turtle import Turtle


class Crossing(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.y_pos = -280
        self.x_pos = 0
        self.goto(self.x_pos, self.y_pos)
        self.showturtle()

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def reset_pos(self):
        self.goto(0, -280)
