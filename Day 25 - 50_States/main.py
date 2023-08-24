import turtle

import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
list_data = data.state.to_list()
guess_state = []
while len(guess_state) < 58:
    answer_state = screen.textinput(f"{len(guess_state)}/58 States", "What's another state's name ?").title()
    print(answer_state)

    if answer_state == "Exit".title():
        missing_state = []
        for state in list_data:
            if state not in guess_state:
                missing_state.append(state)
        new_missing_state = pandas.DataFrame(missing_state)
        new_missing_state.to_csv("new_missing_states.csv")
        break

    # if answer_state is one of the list of states
    if answer_state in list_data:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
    #      create a turtle to write the name of state at state's x and state's y
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]),int(state_data.y.iloc[0]))
        t.write(state_data.state.item())


screen.exitonclick()