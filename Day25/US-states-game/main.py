import turtle
import pandas as pd

# screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# import that data
states_data = pd.read_csv("50_states.csv")
states_list = states_data['state'].to_list()  # get the list of states
x_cors = states_data['x'].to_list()  # get the x coordinates
y_cors = states_data['y'].to_list()  # get the y coordinates

# create a turtle instance
write_turtle = turtle.Turtle()
write_turtle.penup()
write_turtle.hideturtle()

score = 0
correct_guesses = []
while score < 50:
    # get user input
    user_answer = screen.textinput(title=f"{score}/50 Guess the state", prompt="Enter a state's name").title()

    # check if user input is a state in the US
    if user_answer in states_list and user_answer not in correct_guesses:
        state_index = states_list.index(user_answer)  # get the index
        x_cor = x_cors[state_index]  # get the x coordinate
        y_cor = y_cors[state_index]  # get the y coordinate
        write_turtle.goto(x_cor, y_cor)  # go to the position
        write_turtle.write(user_answer)  # write the state
        score += 1  # increment the score
        correct_guesses.append(user_answer)  # add user answer to correct guesses list.

screen.exitonclick()
