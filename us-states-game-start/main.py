import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S State Name")
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data["state"].to_list()

guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title="Guess the state",
                                    prompt="Whats another state name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_state:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data["state"] == answer_state]
        x_int = int(state_data.x)
        y_int = int(state_data.y)
        t.goto(x_int, y_int)
        t.write(state_data["state"].item())


