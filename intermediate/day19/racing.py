from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
y_pos = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
racing = False
turtles = []

#set starting positions for the 6 turtles
for turtle_num in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_num])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_num])
    turtles.append(new_turtle)


if user_bet:
    racing = True

while racing:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You won! The {winning_color} turtle won the race.")
            else:
                print(f"You lost! The {winning_color} turtle won the race.")
            racing = False
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()