import turtle
import pandas

FONT = ("Arial", 12, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def add_state_to_map(state):
    pos = states.index(state)
    x = x_coors[pos]
    y = y_coors[pos]
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.setpos(x, y)
    t.write(state, align="left", font=FONT)


data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()
x_coors = data["x"].tolist()
y_coors = data["y"].tolist()

states_correct = 0
correct_guesses = []

while states_correct < 50:
    answer_state = screen.textinput(f"{states_correct}/50 States Correct", "What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_guesses]
        # missing_states = []
        # for state in states:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if answer_state in states and answer_state not in correct_guesses:
        add_state_to_map(answer_state)
        states_correct += 1
        correct_guesses.append(answer_state)
        if states_correct == 50:
            turtle.write("YOU WIN!", align="center", font=("Arial", 30, "normal"))
            screen.exitonclick()
