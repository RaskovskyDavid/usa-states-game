import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) <= len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                    prompt="What's another state's name? ").title()
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states ]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


    # def get_mouse_click_coor(x, y):
    #     print(x, y)
    # t.write(state_data.state.item())
# turtle.onscreenclick(get_mouse_click_coor)


# turtle.mainloop()
# screen.exitonclick()
